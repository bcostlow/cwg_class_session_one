

dogs = ['husky', 'beagle', 'doberman', 'dachsund', 'collie', 'mutt']

cats = ['siamese', 'burmese', 'angora', 'maine coon', 'manx']

# Bad!
for i in range(min(len(cats), len(dogs))):
    print("Would you like a {} or a {}".format(cats[i], dogs[i]))

print("")

# Good!
for cat, dog in zip(cats, dogs):
    print("Would you like a {} or a {}".format(cat, dog))
