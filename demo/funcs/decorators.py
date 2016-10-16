# Remember, functions are first class
# Which means a function can not only take a function as args
# It can return one, too
import time

def make_adder(add_value):
    def adder(other_value):
        return add_value + other_value
    return adder

add3 = make_adder(3)

print(add3(2))
print(add3(3))
print(add3(4))

# we just demonstrated a closure
# the inner function closes over the outer argument
# used inside the inner


# we can combine funcs as args and as return vals to make a decorator
def timing(some_function):
    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        print("function time: {}".format(str((t2 - t1))))
    return wrapper


def long_func():
    num_list = []
    for num in (range(0, 10000000)):
        num_list.append(num)

long_func = timing(long_func)
long_func()


@timing
def long_func_too():
    num_list = []
    for num in (range(0, 20000000)):
        num_list.append(num)

long_func_too()


# we can also modify the output of a function
def add_honors(some_function):
    def wrapper():
        return [line.strip() + " is a jolly good person!" for line in some_function()]
    return wrapper


@add_honors
def get_names():
    with open('names.txt') as file:
        return file.readlines()

for line in get_names():
    print(line)
