class ClassDemo(object):

    data = "The quick brown fox."

    _sorta_private = "Not Really"

    __almost_private = "Almost Hidden"

    @classmethod
    def print_almost_private(cls):
        print(cls.__almost_private)

print(ClassDemo.data)
print(ClassDemo._sorta_private)
print(ClassDemo.__almost_private)

ClassDemo.print_almost_private()

a = ClassDemo()
b = ClassDemo()
a.data = "Changed"
b._sorta_private = "Also Changed"

print(b.data)
print(a._sorta_private)

a.foo = "baz"
ClassDemo.data = "Changed"
ClassDemo._sorta_private = "Changed"

print(b.data)
print(a._sorta_private)
print(a.foo)