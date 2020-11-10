from flask_socketio import SocketIO
from .api import create_api


def create_app(app):
    app.socketio = SocketIO(app, logger=True)
    create_api(app)
