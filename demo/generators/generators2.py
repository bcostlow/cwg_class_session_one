# More chaining
# Courtesy of my friend Jim Prior


def even_fibonacci(last):
        a = 0
        b = 1
        while True:
            c = a + b
            a = b
            b = c
            if b > last:
                break
            if b % 2 == 0:
                yield b

# much better, break into individual generators and combine as neded


def gen_fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b


def gen_even(gen):
    for number in gen:
        if number % 2 == 0:
            yield number


def gen_lte(gen, max):
    for number in gen:
        if number > max:
            break
        yield number

# Now it's easy to combine generators in different ways.

for num in gen_lte(gen_even(gen_fibonacci()), 20):
    print(num)

print("")

for num in gen_lte(gen_fibonacci(), 1000):
    print(num)
