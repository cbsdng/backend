from json import dumps

from redis import StrictRedis

from .broker import celery


@celery.task(bind=True)
def websocket(self):
    data = {'payload': 'stringilinging'}
    message = dumps(data)
    redis = StrictRedis(host='redis')
    redis.publish('cbsdng', message)
