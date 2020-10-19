from flask import current_app
from flask_smorest import Blueprint, abort
from freenit.api.methodviews import ProtectedMethodView
from freenit.schemas.paging import PageInSchema

from ..models.instance import Instance
from ..schemas.instance import InstancePageOutSchema, InstanceSchema

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


@blueprint.route('/<int:instance_id>', endpoint='detail')
class InstanceAPI(ProtectedMethodView):
    @blueprint.response(InstanceSchema)
    def get(self, instance_id):
        """Get instance details"""
        try:
            instance = Instance.get(id=instance_id)
        except Instance.DoesNotExist:
            abort(404, message='No such instance')
        return instance

    @blueprint.arguments(InstanceSchema(partial=True))
    @blueprint.response(InstanceSchema)
    def patch(self, args, instance_id):
        """Edit instance details"""
        try:
            instance = Instance.get(id=instance_id)
        except Instance.DoesNotExist:
            abort(404, message='No such instance')
        for field in args:
            setattr(instance, field, args[field])
        instance.save()
        return instance

    @blueprint.response(InstanceSchema)
    def delete(self, instance_id):
        """Delete instance"""
        try:
            instance = Instance.get(id=instance_id)
        except Instance.DoesNotExist:
            abort(404, message='No such instance')
        instance.delete_instance()
        return instance
