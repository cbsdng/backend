class Message():
    def __init__(self, id=0, type=0, payload=''):
        self._id = id
        self._type = type
        self._payload = payload

    def __str__(self):
        size = len(self._payload)
        return f'{self._id} {self._type} {self._payload}'

    def __unicode__(self):
        return self.__str__()

    def parse(self, data):
        result = ''
        strpos = data.find(' ')
        pos = int(strpos)
        oldpos = 0
        self._id = int(data[oldpos:pos])
        oldpos = pos
        strpos = data.find(' ', pos + 1)
        pos = int(strpos)
        self._type = int(data[oldpos:pos])
        self._payload = data[pos + 1:]
