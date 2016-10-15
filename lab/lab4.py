# Clean up the class to make it more pythonic

class MyDemoClass(object):

    def __init__(self, data, filename="names.txt"):
        self._data = data
        self._filename = filename
        self._file_contents = ""

    def set_data(data):
        self.data = data

    def get_data(data):
        return self.data

    def compare(self):
        return self._data == self._file_contents

    @property
    def file_contents(self):
        if not self._file_contents:
            file = open(self._filename)
            self._file_contents = file.read()
            file.close()
        return self._file_contents

mdc = MyDemoClass("Random String")
print(mdc.file_contents)
print(mdc.compare())
