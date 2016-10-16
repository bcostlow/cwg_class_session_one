words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']


word_lengths = list(map(len, words))

comp_word_lengths = [len(word) for word in words]

print(word_lengths)
print(comp_word_lengths)
