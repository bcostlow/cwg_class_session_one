
owner_dog = {'Bob': 'chihuahua', 'Jane': 'mastiff', 'Bill': 'German Shepard', 'Kate': 'poodle'}


# To get the keys, iterate as over a sequence

for key in owner_dog:
    print(key)

print("")

# make another dict as this is evil
owner_dog2 = {'Bob': 'chihuahua', 'Jane': 'mastiff', 'Bill': 'German Shepard', 'Kate': 'poodle'}

# Need to put in a try, as this is evil.
try:
    for key in owner_dog2:
        if key == 'Jane':
            del(owner_dog2[key])
except RuntimeError as error:
    print("Error: {}".format(error))

print("")

# proper way to do things.
for key in list(owner_dog.keys()):
    if key == 'Jane':
            del(owner_dog[key])

print("")

# you can get keys and values like this
for owner in owner_dog:
    print("{} owns a {}".format(owner, owner_dog[owner]))

print("")

# this is more efficient and a little clearer
for owner, breed in owner_dog.items():
    print("{} owns a {}".format(owner, breed))
