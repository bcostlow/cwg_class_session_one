"""Looping Examples"""

dogs = ['husky', 'beagle', 'doberman', 'dachsund', 'collie', 'mutt']

# Reversing

# range takes additional step and stop args,
# stop val is exclusive
# so range(5, -1, -1) --> [5, 4, 3, 2, 1, 0]
# This leads to this kind of code
# Bad!
for i in range(len(dogs) - 1, -1, -1):
    print(dogs[i])

print('')

# Pythonic! Use the built-ins
for dog in reversed(dogs):
    print(dog)

print('')

# Pythonic sorting
for dog in sorted(dogs):
    print(dog)

print('')

# but don't
for dog in reversed(sorted(dogs)):
    print(dog)

print('')

# because this
for dog in sorted(dogs, reverse=True):
    print(dog)
