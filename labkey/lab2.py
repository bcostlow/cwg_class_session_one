# Here is the code from the generators2.py file
# From the demo
# Can you refactor any or all of it to use comprehensions?

# More chaining
# Courtesy of my friend Jim Prior


def gen_fibonacci():
    a, b = 0, 1
    while True:
       a, b = b, a + b
       yield b

def gen_even(gen):
    return (number for number in gen if number % 2 == 0)

def error():
    raise StopIteration

def gen_lte(gen, max):
    return (error() if number > max else number for number in gen)

# Now it's easy to combine generators in different ways.

for num in gen_lte(gen_even(gen_fibonacci()), 20):
    print(num)

print("")

for num in gen_lte(gen_fibonacci(), 1000):
    print(num)
