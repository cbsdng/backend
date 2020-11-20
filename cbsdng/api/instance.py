from flask import current_app
from flask_smorest import Blueprint
from freenit.api.methodviews import ProtectedMethodView
from freenit.schemas.paging import PageInSchema

from ..models.instance import Instance
from ..schemas.instance import InstancePageOutSchema, InstanceSchema
from ..tasks.instance import start, stop

blueprint = Blueprint('instances', 'instances')


@blueprint.route('', endpoint='list')
class InstanceListAPI(ProtectedMethodView):
    @blueprint.arguments(PageInSchema(), location='headers')
    @blueprint.response(InstancePageOutSchema)
    def get(self, pagination):
        """List instances"""
        instances = Instance.fetchAll(current_app.config['SOCKET'])
        result = {
            'data': [i.data() for i in instances],
            'total': len(instances),
            'pages': 1,
        }
        return result

    @blueprint.arguments(InstanceSchema)
    @blueprint.response(InstanceSchema)
    def post(self, args):
        """Create instance"""
        instance = Instance(**args)
        instance.save()
        return instance


@blueprint.route('/<instance_name>/start', endpoint='start')
class InstanceStartAPI(ProtectedMethodView):
    @blueprint.response(InstanceSchema)
    def get(self, instance_name):
        """Start instance"""
        start.delay(instance_name)
        return {}


@blueprint.route('/<instance_name>/stop', endpoint='stop')
class InstanceStopAPI(ProtectedMethodView):
    @blueprint.response(InstanceSchema)
    def get(self, instance_name):
        """Stop instance"""
        stop.delay(instance_name)
        return {}
