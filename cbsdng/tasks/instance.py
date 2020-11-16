#  from json import dumps
from celery import current_app

#  from redis import StrictRedis

from .broker import celery
from ..models.instance import Instance


@celery.task(bind=True)
def start(self, instance_name):
    instance = Instance(
        socketpath=current_app.config['SOCKET'],
        name=instance_name,
    )
    instance.start()
    #  message = dumps(instance.data())
    #  redis = StrictRedis(host='redis')
    #  redis.publish('cbsdng', message)


@celery.task(bind=True)
def stop(self, instance_name):
    instance = Instance(
        socketpath=current_app.config['SOCKET'],
        name=instance_name,
    )
    instance.stop()
