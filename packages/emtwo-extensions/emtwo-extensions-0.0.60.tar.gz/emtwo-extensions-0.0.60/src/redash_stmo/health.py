import json
import time
import redash

from redash_stmo import settings

from flask import jsonify
from flask_login import login_required

from celery.utils.log import get_task_logger
from redash import models, redis_connection, statsd_client
from redash.worker import celery
from redash.utils import parse_human_time
from redash.monitor import get_status as original_get_status
from redash.query_runner import BaseQueryRunner
from redash.handlers.base import routes
from redash.permissions import require_super_admin

logger = get_task_logger(__name__)


def store_health_status(data_source_id, data_source_name, query_text, data):
    key = "data_sources:health"

    cache = json.loads(redis_connection.get(key) or '{}')
    if data_source_id not in cache:
        cache[data_source_id] = {
            "metadata": {"name": data_source_name},
            "queries": {}
        }
    cache[data_source_id]["queries"][query_text] = data

    cache[data_source_id]["status"] = "SUCCESS"
    for query_status in cache[data_source_id]["queries"].values():
        if query_status["status"] == "FAIL":
            cache[data_source_id]["status"] = "FAIL"
            break

    redis_connection.set(key, json.dumps(cache))


@celery.task(name="redash_stmo.health.update_health_status", time_limit=90, soft_time_limit=60)
def update_health_status():
    for data_source in models.DataSource.query:
        logger.info(u"task=update_health_status state=start ds_id=%s", data_source.id)

        runtime = None
        query_text = data_source.query_runner.noop_query
        custom_queries = settings.CUSTOM_HEALTH_QUERIES
        ds_id = str(data_source.id)

        if custom_queries and ds_id in custom_queries:
            query_text = custom_queries[ds_id]

        try:
            start_time = time.time()
            test_connection(data_source.query_runner, query_text)
            runtime = time.time() - start_time
        except NotImplementedError:
            logger.warning(u"Unable to compute health status without test query for %s", data_source.name)
            continue
        except Exception as e:
            logger.warning(u"Failed health check for the data source: %s", data_source.name, exc_info=1)
            statsd_client.incr('update_health_status.error')
            logger.info(u"task=update_health_status state=error ds_id=%s runtime=%.2f", data_source.id, time.time() - start_time)

        status = {
            "status": "SUCCESS" if runtime is not None else "FAIL",
            "last_run": start_time,
            "last_run_human": str(parse_human_time(str(start_time))),
            "runtime": runtime
        }
        store_health_status(ds_id, data_source.name, query_text, status)


def test_connection(self, custom_query_text=None):
    if self.noop_query is None:
        raise NotImplementedError()

    query_text = custom_query_text or self.noop_query
    data, error = self.run_query(query_text, None)

    if error is not None:
        raise Exception(error)

@login_required
@require_super_admin
def stmo_status_api():
    status = original_get_status()
    status['data_sources'] = json.loads(redis_connection.get('data_sources:health') or '{}')
    return jsonify(status)


from redash.worker import celery_schedule
from . import settings





def datasource_health(app=None):
    app.view_functions['%s.status_api' % routes.name] = stmo_status_api

    '''
    task_info = {
        "task": update_health_status,
        "interval_in_seconds": settings.HEALTH_QUERIES_REFRESH_SCHEDULE
    }
    '''
    celery_schedule['update_health_status'] = {
        'task': 'redash_stmo.health.update_health_status',  # the Celery task
        'schedule': timedelta(minutes=settings.HEALTH_QUERIES_REFRESH_SCHEDULE)
    }
    celery.conf.update(CELERYBEAT_SCHEDULE=celery_schedule)

    #return task_info

