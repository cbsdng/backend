from freenit.api import register_endpoints


def create_api(app):
    from .instance import blueprint as instance
    register_endpoints(
        app,
        '/api/v0',
        [
            instance,
        ],
    )
