import socket

from ..types import Type
from .message import Message


class Instance():
    sock = None

    def __init__(self, **kwargs):
        self.sockpath = kwargs.get('sockpath', None)
        self.name = kwargs.get('name', '')
        self.id = kwargs.get('id', 0)
        self.ip = kwargs.get('ip', '')
        self.hostname = kwargs.get('hostname', '')
        self.path = kwargs.get('path', '')
        self.state = kwargs.get('state', 'Off')
        self.ram = kwargs.get('ram', 0)
        self.curmem = kwargs.get('curmem', 0)
        self.cpus = kwargs.get('cpus', 1)
        self.pcpu = kwargs.get('pcpu', 0)
        self.ostype = kwargs.get('ostype', '')
        self.vnc = kwargs.get('vnc', '')
        self.type = kwargs.get('type', 'jail')
        if self.sockpath is not None:
            self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.sock.connect(self.sockpath)

    @classmethod
    def fetchAll(cls, sockpath):
        cls.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        cls.sock.connect(sockpath)
        command = Message(0, Type.NOCOLOR, 'ls header=0')
        data = str(command)
        cls.sock.sendall(bytes(data, 'utf-8'))
        buffer = cls.sock.recv(1024)
        data = buffer.decode('utf-8')
        message = Message()
        message.parse(data)
        instances = []
        for m in message._payload.split('\n'):
            tokens = [token for token in m.split() if token != '']
            if (len(tokens) == 6):
                i = Instance()
                i.name, i.id, i.ip, i.hostname, i.path, i.state = tokens
                i.type = 'jail'
                instances.append(i)
        cls.sock.close()

        cls.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        cls.sock.connect(sockpath)
        command = Message(0, Type.BHYVE | Type.NOCOLOR, 'ls header=0')
        data = str(command)
        cls.sock.sendall(bytes(data, 'utf-8'))
        buffer = cls.sock.recv(1024)
        data = buffer.decode('utf-8')
        message = Message()
        message.parse(data)
        for m in message._payload.split('\n'):
            tokens = [token for token in m.split() if token != '']
            if (len(tokens) == 10):
                i = Instance()
                i.name, i.id, i.ram, i.curmem, i.cpus, i.pcpu, i.ostype, i.ip, i.state, i.vnc = tokens
                i.type = 'bhyve'
                instances.append(i)

        cls.sock.close()
        return instances

    def __str__(self):
        return f'{self.name} {self.id}'

    def __repr__(self):
        return self.__str__()

    def data(self):
        if self.type == 'bhyve':
            return {
                'id': self.id,
                'name': self.name,
                'ram': self.ram,
                'curmem': self.curmem,
                'pcpu': self.pcpu,
                'ostype': self.ostype,
                'ip': self.ip,
                'state': self.state,
                'vnc': self.vnc,
            }
        else:
            return {
                'id': self.id,
                'name': self.name,
                'ip': self.ip,
                'hostname': self.hostname,
                'path': self.path,
                'state': self.state,
            }
