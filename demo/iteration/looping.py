"""Looping Examples"""

dogs = ['husky', 'beagle', 'doberman', 'dachsund', 'collie', 'mutt']

# This is an abomination! Who would do something like this?
i = 0; max = len(dogs)
while i < max:
    print(dogs[i])
    i += 1

print("")

# This is better, for some value of better
# compared to above, but NOT Pythonic!
for i in range(len(dogs)):
    print(dogs[i])

print("")

# pythonic
for dog in dogs:
    print(dog)
