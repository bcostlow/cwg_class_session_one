# Entire example what for x in sequence does

dogs = ['husky', 'beagle', 'doberman', 'dachsund', 'collie', 'mutt']

# This
for dog in dogs:
    print(dog)

print("")

# Is basically
dog_iterator = iter(dogs)
while True:
    try:
        print(next(dog_iterator))
    except StopIteration:
        break
