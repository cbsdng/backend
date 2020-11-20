from flask_smorest import Blueprint
from freenit.api.methodviews import MethodView

from ..schemas.websocket import WebSocketSchema
from ..tasks.websocket import websocket

blueprint = Blueprint('websockets', 'websockets')


@blueprint.route('', endpoint='list')
class WebSocketListAPI(MethodView):
    @blueprint.response(WebSocketSchema)
    def get(self):
        """List websockets"""
        websocket.delay()
        return {
            'status': 'OK',
        }
