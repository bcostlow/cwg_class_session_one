# some file play


def old_print_file(file_path):
    file = open(file_path)
    while True:
        line = file.readline()
        if line:
            print(line)
        else:
            break
    file.close()

old_print_file('names.txt')
print("---------------------\n")


def print_file(file_path):
    file = open(file_path)
    for line in file:  # file objects support the iterator protocol! It's lazy like a generator.
        print(line)
    file.close()

print_file('names.txt')
print("---------------------\n")


def best_print_file(file_path):
    with open(file_path) as file:  # This is a context manager, more about those later.
        for line in file:
            print(line)

best_print_file('names.txt')
