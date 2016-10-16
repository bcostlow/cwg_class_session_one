# Clean up the class to make it more pythonic

class MyDemoClass(object):

    def __init__(self, data, filename="names.txt"):
        self.data = data
        self.filename = filename
        self.file_contents = ""

    def load_file(self):
        if not self.file_contents:
            with open(self.filename) as file:
                self.file_contents = file.read()

    def compare(self):
        return self.data == self.file_contents

mdc = MyDemoClass("Random String")
mdc.load_file()
print(mdc.file_contents)
print(mdc.compare())

print("--------------------------")
# but even better
def compare_and_print(file, data):
    contents = file.read()
    print(contents)
    print(contents == data)

with open("names.txt") as file:
    compare_and_print(file, "Random String")
