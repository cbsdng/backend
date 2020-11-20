import sys


class Message():
    def __init__(self, id=0, type=0, payload=''):
        self.id = id
        self.type = type
        self.payload = payload

    def __str__(self):
        return f'{self.id} {self.type} {self.payload}'

    def __unicode__(self):
        return self.__str__()

    @classmethod
    def receive(cls, socket):
        message = Message()
        buffer = socket.recv(4)
        if len(buffer) == 0:
            message.type = -1
            return message
        message.id = int.from_bytes(buffer, sys.byteorder)
        buffer = socket.recv(4)
        if len(buffer) == 0:
            message.type = -1
            return message
        message.type = int.from_bytes(buffer, sys.byteorder)
        buffer = socket.recv(4)
        if len(buffer) == 0:
            message.type = -1
            return message
        size = int.from_bytes(buffer, sys.byteorder)
        buffer = socket.recv(size)
        if len(buffer) == 0:
            message.type = -1
            return message
        message.payload = buffer.decode('utf-8')
        return message

    def dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'payload': self.payload,
        }

    def send(self, socket):
        socket.sendall(self.id.to_bytes(4, sys.byteorder))
        socket.sendall(self.type.to_bytes(4, sys.byteorder))
        socket.sendall(len(self.payload).to_bytes(4, sys.byteorder))
        socket.sendall(bytes(self.payload, 'utf-8'))
