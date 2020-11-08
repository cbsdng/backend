from importlib import import_module

from freenit import create_app

from config import configs
from name import app_name


def init(config_name):
    api = import_module(f'{app_name}.api')
    config = configs[config_name]
    application = create_app(config)
    api.create_api(application)
    return application
