import os

from application import init

config_name = os.getenv('FLASK_ENV', 'default')
application = init(config_name, False)
celery = application.celery
