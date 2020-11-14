from flask_socketio import SocketIO

from .api import create_api
from .tasks.broker import make_celery
from .websocket import WebSocketThread


def create_app(app, websocket=True):
    if websocket:
        app.socketio = SocketIO(
            app,
            logger=True,
            message_queue='redis://redis',
        )
        app.websocket_thread = WebSocketThread(app.socketio, 'redis')
        app.websocket_thread.start()
    app.celery = make_celery(app)
    create_api(app)
