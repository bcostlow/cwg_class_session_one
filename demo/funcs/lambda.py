# Don't get excited, not real lambda.
# Inline anonymous function. One line, One statement.

# These are the same.
def add_two(x):
    return x + 2

# But don't do this one!
another_add_2 = lambda x: x + 2

vals = [1, 2, 3]

multiplied = map(lambda x: x + 2, vals)
also_multiplied = [x + 2 for x in vals]  # comprehension generally preferred


# So why?
# Only things I ever use them for
# Args and default args for function that expects a function as args
def data_handler(data, validator=lambda x: x):
    clean = validator(data)
    print(clean)

data_handler('some text')

data_handler('some text', lambda x: x.upper())

# callbacks
