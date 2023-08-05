from guillotina.commands import Command
from guillotina.db import ROOT_ID, TRASHED_ID
from guillotina.commands.utils import change_transaction_strategy
from guillotina.component import getUtility
from guillotina.db.reader import reader
from guillotina.interfaces import ICatalogUtility
from guillotina.utils import get_containers
from guillotina_elasticsearch.migration import Migrator
from lru import LRU  # pylint: disable=E0611

import aioes
import asyncio
import json
import logging

try:
    from guillotina.utils import clear_conn_statement_cache
except ImportError:
    def clear_conn_statement_cache(conn):
        pass

logger = logging.getLogger('guillotina_elasticsearch_vacuum')

SELECT_BY_KEYS = '''SELECT zoid from objects where zoid = ANY($1)'''
BATCHED_GET_CHILDREN_BY_PARENT = """
SELECT zoid, parent_id
FROM objects
WHERE of is NULL AND parent_id = ANY($1)
ORDER BY parent_id
LIMIT $2::int
OFFSET $3::int
"""

PAGE_SIZE = 1000

GET_OBS_BY_TID = f"""
SELECT zoid, tid, parent_id
FROM objects
WHERE
    of is NULL AND
    tid >= $1
ORDER BY tid ASC, zoid ASC
LIMIT {PAGE_SIZE}
"""

GET_ALL_FOR_TID = f"""
SELECT zoid, parent_id, tid
FROM objects
WHERE
    of is NULL AND
    tid = $1 and zoid > $2
ORDER BY zoid ASC
LIMIT {PAGE_SIZE}
"""

CREATE_INDEX = '''
CREATE INDEX CONCURRENTLY IF NOT EXISTS
objects_tid_zoid ON objects (tid ASC, zoid ASC);'''


class Vacuum:

    def __init__(self, txn, tm, request, container, last_tid=-2,
                 index_scroll='15m', hits_scroll='5m', use_tid_query=True):
        self.txn = txn
        self.tm = tm
        self.request = request
        self.container = container
        self.orphaned = []
        self.missing = []
        self.utility = getUtility(ICatalogUtility)
        self.migrator = Migrator(
            self.utility, self.container, full=True, bulk_size=10)
        self.cache = LRU(200)
        self.last_tid = last_tid
        self.use_tid_query = use_tid_query
        self.last_zoid = None
        # for state tracking so we get boundries right
        self.last_result_set = []
        self.index_scroll = index_scroll
        self.hits_scroll = hits_scroll

    async def iter_batched_es_keys(self):
        index_name = await self.utility.get_index_name(self.container)
        result = await self.utility.conn.search(
            index=index_name,
            scroll=self.index_scroll,
            size=PAGE_SIZE,
            _source=False,
            body={
                "sort": ["_doc"]
            })
        yield [r['_id'] for r in result['hits']['hits']]
        scroll_id = result['_scroll_id']
        while scroll_id:
            try:
                result = await self.utility.conn.scroll(
                    scroll_id=scroll_id,
                    scroll=self.hits_scroll
                )
            except aioes.exception.TransportError:
                # no results
                break
            if len(result['hits']['hits']) == 0:
                break
            yield [r['_id'] for r in result['hits']['hits']]
            scroll_id = result['_scroll_id']

    async def get_db_page_of_keys(self, oids, page=1, page_size=PAGE_SIZE):
        conn = await self.txn.get_connection()
        clear_conn_statement_cache(conn)
        async with self.txn._lock:
            return await conn.fetch(
                BATCHED_GET_CHILDREN_BY_PARENT, oids,
                page_size, (page - 1) * page_size)

    async def get_page_from_tid(self):
        conn = await self.txn.get_connection()
        clear_conn_statement_cache(conn)
        records = []
        queried_tid = self.last_tid
        async with self.txn._lock:
            results = await conn.fetch(GET_OBS_BY_TID, queried_tid)
            for record in results:
                if record['zoid'] in (ROOT_ID, TRASHED_ID, self.container._p_oid):
                    continue
                records.append(record)
                self.last_tid = record['tid']
                self.last_zoid = record['zoid']
        if len(records) == 0:
            if len(self.last_result_set) > 0:
                # now we have zero, increment, but only once
                self.last_tid = self.last_tid + 1
        self.last_result_set = records
        return records

    async def iter_paged_db_keys(self, oids):
        if self.use_tid_query:
            queried_tid = self.last_tid
            records = await self.get_page_from_tid()
            while len(records) > 0:
                yield records
                if self.last_tid == queried_tid:
                    conn = await self.txn.get_connection()
                    logger.warning(f'Getting all keys from tid {self.last_tid}')
                    # we're stuck on same tid, get all for this tid
                    # and then move on...
                    clear_conn_statement_cache(conn)
                    results = await conn.fetch(
                        GET_ALL_FOR_TID, self.last_tid, self.last_zoid)
                    while len(results) > 0:
                        records = []
                        for record in results:
                            if record['zoid'] in (ROOT_ID, TRASHED_ID, self.container._p_oid):
                                continue
                            records.append(record)
                            self.last_zoid = record['zoid']
                        yield records
                        clear_conn_statement_cache(conn)
                        records = await conn.fetch(
                            GET_ALL_FOR_TID, self.last_tid, self.last_zoid)
                    self.last_tid = self.last_tid + 1
                queried_tid = self.last_tid
                records = await self.get_page_from_tid()

        else:
            page_num = 1
            page = await self.get_db_page_of_keys(oids, page_num)
            while page:
                yield page
                async for sub_page in self.iter_paged_db_keys(
                        [r['zoid'] for r in page]):
                    yield sub_page
                page_num += 1
                page = await self.get_db_page_of_keys(oids, page_num)

    async def get_object(self, oid):
        if oid in self.cache:
            return self.cache[oid]

        try:
            result = self.txn._manager._hard_cache.get(oid, None)
        except AttributeError:
            from guillotina.db.transaction import HARD_CACHE  # pylint: disable=E0611
            result = HARD_CACHE.get(oid, None)
        if result is None:
            clear_conn_statement_cache(await self.txn.get_connection())
            result = await self.txn._cache.get(oid=oid)

        if result is None:
            result = await self.tm._storage.load(self.txn, oid)

        obj = reader(result)
        obj._p_jar = self.txn
        if result['parent_id']:
            obj.__parent__ = await self.get_object(result['parent_id'])
        return obj

    async def process_missing(self, oid, folder=False):
        # need to fill in parents in order for indexing to work...
        logger.warning(f'Index missing {oid}')
        try:
            obj = await self.get_object(oid)
        except KeyError:
            logger.warning(f'Could not find {oid}')
            return
        except (AttributeError, TypeError):
            logger.warning(f'Could not find {oid}', exc_info=True)
            return  # object or parent of object was removed, ignore
        try:
            if folder:
                await self.migrator.process_object(obj)
            else:
                await self.migrator.index_object(obj)
        except TypeError:
            logger.warning(f'Could not reindex {oid}')

    async def setup(self):
        # how we're doing this...
        # 1) iterate through all es keys
        # 2) batch check obs exist in db
        # 3) iterate through all db keys
        # 4) batch check they are in elasticsearch
        # WHY this way?
        #   - uses less memory rather than getting all keys in both.
        #   - this way should allow us handle VERY large datasets

        try:
            conn = await self.txn.get_connection()
            await conn.execute(CREATE_INDEX)
        except Exception:
            pass

        self.index_name = await self.utility.get_index_name(self.container)
        self.migrator.work_index_name = self.index_name

    async def check_orphans(self):
        logger.warning(f'Checking orphans on container {self.container.id}', extra={
            'account': self.container.id
        })
        conn = await self.txn.get_connection()
        checked = 0
        async for es_batch in self.iter_batched_es_keys():
            checked += len(es_batch)
            clear_conn_statement_cache(conn)
            async with self.txn._lock:
                records = await conn.fetch(SELECT_BY_KEYS, es_batch)
            db_batch = set()
            for record in records:
                db_batch.add(record['zoid'])
            orphaned = [k for k in set(es_batch) - db_batch]
            if checked % 10000 == 0:
                logger.warning(f'Checked ophans: {checked}')
            if orphaned:
                # these are keys that are in ES but not in DB so we should
                # remove them..
                self.orphaned.extend(orphaned)
                logger.warning(f'deleting orphaned {len(orphaned)}')
                conn_es = await self.utility.conn.transport.get_connection()
                # delete by query for orphaned keys...
                await conn_es._session.post(
                    '{}{}/_delete_by_query'.format(
                        conn_es._base_url.human_repr(),
                        self.index_name),
                    data=json.dumps({
                        'query': {
                            'terms': {
                                'uuid': orphaned
                            }
                        }
                    }))

    async def check_missing(self):
        status = (f'Checking missing on container {self.container.id}, '
                  f'starting with TID: {self.last_tid}')
        logger.warning(status, extra={
            'account': self.container.id
        })
        conn = await self.txn.get_connection()
        if self.use_tid_query:
            # if it's enabled, check to see if we can
            containers = await conn.fetch(
                'select zoid from objects where parent_id = $1', ROOT_ID)
            if len(containers) > 1:
                # more than 1 container, we can't optimize by querying by tids
                self.use_tid_query = False

        checked = 0
        async for batch in self.iter_paged_db_keys([self.container._p_oid]):
            oids = [r['zoid'] for r in batch]
            results = await self.utility.conn.search(
                self.index_name, body={
                    'query': {
                        'terms': {
                            'uuid': oids
                        }
                    }
                },
                _source=True,
                size=PAGE_SIZE)

            es_batch = {}
            for result in results['hits']['hits']:
                oid = result['_id']
                es_batch[oid] = {
                    'parent_uuid': result['_source'].get('parent_uuid') or '_missing_'
                }

            for record in batch:
                oid = record['zoid']
                if oid == self.container._p_oid:
                    continue
                if oid not in es_batch:
                    self.missing.append(oid)
                    await self.process_missing(oid)
                elif record['parent_id'] != es_batch[oid]['parent_uuid']:
                    self.missing.append(oid)
                    await self.process_missing(oid, folder=True)

            checked += len(batch)
            logger.warning(
                f'Checked missing: {checked}: {self.last_tid}, '
                f'missing: {len(self.missing)}')

        await self.migrator.flush()
        await self.migrator.join_futures()


class VacuumCommand(Command):
    description = 'Run vacuum on elasticearch'
    vacuum_klass = Vacuum
    state = {}

    def get_parser(self):
        parser = super(VacuumCommand, self).get_parser()
        parser.add_argument(
            '--continuous', help='Continuously vacuum', action='store_true')
        parser.add_argument(
            '--disable-tid-query', help='Disable tid query', action='store_true')
        parser.add_argument('--sleep', help='Time in seconds to sleep',
                            default=10 * 60, type=int)
        return parser

    async def run(self, arguments, settings, app):
        change_transaction_strategy('none')
        self.request._db_write_enabled = True
        self.request._message.headers['Host'] = 'localhost'
        await asyncio.gather(
            self.do_check(arguments, 'check_missing'),
            self.do_check(arguments, 'check_orphans'))

    async def do_check(self, arguments, check_name):
        first_run = True
        while arguments.continuous or first_run:
            if not first_run:
                await asyncio.sleep(arguments.sleep)
            else:
                first_run = False
            async for txn, tm, container in get_containers(self.request):
                try:
                    kwargs = {}
                    if container._p_oid in self.state:
                        kwargs = self.state[container._p_oid]

                    if arguments.scroll:
                        kwargs.update({
                            'index_scroll': arguments.scroll,
                            'hits_scroll': arguments.scroll
                        })
                    if arguments.disable_tid_query:
                        kwargs['use_tid_query'] = False

                    vacuum = self.vacuum_klass(
                        txn, tm, self.request, container, **kwargs)
                    await vacuum.setup()
                    func = getattr(vacuum, check_name)
                    await func()
                    if vacuum.last_tid > 0:
                        self.state[container._p_oid] = {
                            'last_tid': vacuum.last_tid
                        }
                    logger.warning(f'''Finished vacuuming with results:
Orphaned cleaned: {len(vacuum.orphaned)}
Missing added: {len(vacuum.missing)}
''')
                except Exception:
                    logger.error('Error vacuuming', exc_info=True)
                finally:
                    await tm.abort(txn=txn)
