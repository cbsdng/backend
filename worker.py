import os
from application import init
from cbsdng.tasks import make_celery

config_name = os.getenv('FLASK_ENV', 'default')
application = init(config_name)
celery = make_celery(application)
