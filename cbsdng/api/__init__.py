from freenit.api import register_endpoints


def create_api(app):
    from .instance import blueprint as instance
    from .plan import blueprint as plan
    register_endpoints(
        app,
        '/api/v0',
        [
            instance,
            plan,
        ],
    )
