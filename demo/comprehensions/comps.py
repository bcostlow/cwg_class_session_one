words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']


def get_word_lengths(word_list):
    lengths = list()
    for word in word_list:
        lengths.append(len(word))
    return lengths

word_lengths = get_word_lengths(words)

comp_word_lengths = [len(word) for word in words]

print(word_lengths)
print(comp_word_lengths)
