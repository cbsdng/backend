from flask_socketio import SocketIO

from .api import create_api
from .websocket import WebSocketThread


def create_app(app):
    app.socketio = SocketIO(app, logger=True, message_queue='redis://redis')
    app.websocket_thread = WebSocketThread(app.socketio, 'redis')
    app.websocket_thread.start()
    create_api(app)
