words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
words2 = ['have', 'you', 'seen', 'a', 'blue', 'fish']

# what if we did the first example as a generator?


def get_word_lengths(word_list):
    for word in word_list:
        yield len(word)

for length in get_word_lengths(words):
    print(length)

print('--------------------')

for length in (len(word) for word in words):
    print(length)
