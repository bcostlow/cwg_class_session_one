def this_is_a_func():
    print("We've been using them all class\n")


def funcs_are_first_class(other_func):
    print("How long have we been using them?\n")
    other_func()

funcs_are_first_class(this_is_a_func)

# I can put them in a list (illustrative -- Not idiomatic!)
func_list = [funcs_are_first_class, this_is_a_func]
func_list[0](func_list[1])

# I can put them in a dict (illustrative -- Not idiomatic!)
func_dict = {'a_func': this_is_a_func, 'first_class': funcs_are_first_class}
func_dict['first_class'](func_dict['a_func'])


# this allows for very clean depenency injection patterns
def string_length_and_strings(input, output):
    for string_ in input():
        output("{} {}".format(len(string_), string_))


def file_input():
    with open('names.txt') as f:
        for line in f:
            yield line

string_length_and_strings(file_input, print)

# or...
with open('counts.txt', 'w') as outfile:
    string_length_and_strings(file_input, outfile.write)
