"""Below is a function that opens a file where each line
is firstname lastname (space between).

Refactor this code with what you've learned so far.
"""


def bad_split_names(file_path):
    names = list()
    split_names = list()
    file = open(file_path)
    while True:
        line = file.readline().strip()
        if line:
            names.append(line)
        else:
            break
    file.close()
    for name in names:
        split_names.append(name.split(" "))
    for split_name in split_names:
        print("Last: {}, First: {}".format(split_name[1], split_name[0]))

bad_split_names('names.txt')
