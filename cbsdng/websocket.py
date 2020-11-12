import threading
from json import loads

from redis import StrictRedis


class WebSocketThread(threading.Thread):
    def __init__(self, socketio, redis_host, daemon=True):
        threading.Thread.__init__(self, daemon=daemon)
        self.socketio = socketio
        self.redis = StrictRedis(host=redis_host)
        self.listener = self.redis.pubsub()
        self.listener.subscribe('cbsdng')

    def run(self):
        for message in self.listener.listen():
            if message['type'] == 'message':
                data = loads(message['data'])
                self.socketio.emit('output', data)
