class BadClass(object):

    def __init__(self):
        self.data = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

bad = BadClass()
bad.set_data("Some Stuff")
print(bad.get_data())


class GoodClass(object):

    def __init__(self):
        self.data = ""

good = GoodClass()
good.data = "More Stuff"
print(good.data)


class PropsClass(object):

    def __init__(self):
        self._data = ""

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data.upper()

props = PropsClass()
props.data = "More Stuff"
print(props.data)


class PythonsNotRuby(object):
    """Never Never Never"""
    def __init__(self):
        self._connection = ""

    @property
    def connection(self):
        return self._connection

    @data.setter
    def connection(self):
        self._connection = socket.connect('127.0.0.1', 8080)
