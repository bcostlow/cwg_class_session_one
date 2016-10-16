# But what if I need that number?
dogs = ['husky', 'beagle', 'doberman', 'dachsund', 'collie', 'mutt']

# Bad
for i in range(len(dogs)):
    print("{} is number {}!".format(dogs[i], i + 1))

print("")

# Good
for number, dog in enumerate(dogs):
    print("{} is number {}!".format(dog, number + 1))

print("")

# Better, enumerate takes a start value.
for number, dog in enumerate(dogs, 1):
    print("{} is number {}!".format(dog, number))
