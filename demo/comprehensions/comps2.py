words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
words2 = ['have', 'you', 'seen', 'a', 'blue', 'fish']


def get_unique_intersect(one, two):
    one = set(one)
    two = set(two)
    return one & two

unique_intersect = get_unique_intersect(words, words2)

also_unique_intersect = {word for word in words if word in words2}

print(unique_intersect)
print(also_unique_intersect)
