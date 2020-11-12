from freenit.api import register_endpoints


def create_api(app):
    from .instance import blueprint as instance
    from .plan import blueprint as plan
    from .websocket import blueprint as websocket
    register_endpoints(
        app,
        '/api/v0',
        [
            instance,
            plan,
            websocket,
        ],
    )
