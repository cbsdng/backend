from json import dumps
from flask_smorest import Blueprint
from freenit.api.methodviews import MethodView
from redis import StrictRedis

from ..schemas.websocket import WebSocketSchema

blueprint = Blueprint('websockets', 'websockets')


@blueprint.route('', endpoint='list')
class WebSocketListAPI(MethodView):
    @blueprint.response(WebSocketSchema)
    def get(self):
        """List websockets"""
        data = {'payload': 'stringilinging'}
        message = dumps(data)
        redis = StrictRedis(host='redis')
        redis.publish('cbsdng', message)
        return {
            'status': 'OK',
        }
