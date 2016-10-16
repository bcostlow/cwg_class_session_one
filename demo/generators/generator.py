
dogs = ['husky', 'beagle', 'doberman', 'dachsund', 'collie', 'mutt']


def my_generator(sequence_of_strings):
    count = 0
    max_val = len(sequence_of_strings)
    while True:
        if count < max_val:
            multiplier = count + 1
            spam = "spam, " * multiplier
            yield spam + "and " + sequence_of_strings[count]
            count += 1
        else:
            break

for value in my_generator(dogs):
    print(value)

print("")


# That's pretty ugly, remember no counters, and "business logic"
# better
def my_generator_two(sequence_of_strings):
    for count, value in enumerate(sequence_of_strings):
        multiplier = count + 1
        spam = "spam, " * multiplier
        yield spam + "and " + sequence_of_strings[count]

for value in my_generator_two(dogs):
    print(value)

print("")


# Chaining iterators/generators
def my_generator_three(count_text_pairs):
    for count, text in count_text_pairs:
        spam = "spam, " * (count + 1)
        yield spam + "and " + text

for value in my_generator_three(enumerate(dogs)):
    print(value)

print("")


def string_length_and_string(sequence_of_strings):
    for string_ in sequence_of_strings:
        yield len(string_), string_

for value in my_generator_three(string_length_and_string(dogs)):
    print(value)

print("")

# note, calling the function just returns a generator, it does not do anything
# Until next is called.

gen = my_generator_three(string_length_and_string(dogs))
print(gen)

print("")

for value in gen:
    print(value)
