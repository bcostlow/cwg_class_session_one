"""Below is a function that opens a file where each line
is firstname lastname (space between).

Refactor this code with what you've learned so far.
"""

def get_lines_in_file(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip()

def split_names_into_first_last(names):
    for name in names:
        first_name, last_name = name.split(" ")
        yield first_name, last_name

def print_first_and_last(split_names):
    for first_name, last_name in split_names:
        print("Last: {}, First: {}".format(last_name, first_name))

print_first_and_last(split_names_into_first_last(get_lines_in_file('names.txt')))

