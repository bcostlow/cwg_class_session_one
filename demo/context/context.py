# We've seen this before:


def old_print_file(file_path):
    file = open(file_path)
    while True:
        line = file.readline()
        if line:
            print(line)
        else:
            break
    file.close()

# What's wrong with that code? Besides that it's not pythonic?
# What happens if the function errors?
# We need something like this


def old_print_file_again(file_path):
    try:
        file = open(file_path)
        while True:
            line = file.readline()
            if line:
                print(line)
            else:
                break
    finally:
        file.close()


# This is not only more elegant, it handles the error condition!
def best_print_file(file_path):
    with open(file_path) as file:  # This is a context manager, more about those later.
        for line in file:
            print(line)
    # when we leave the with block the file closes no matter what
