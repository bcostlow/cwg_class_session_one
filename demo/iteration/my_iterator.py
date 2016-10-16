# We can make our own iterators

dogs = ['husky', 'beagle', 'doberman', 'dachsund', 'collie', 'mutt']


class MyIterator(object):

    def __init__(self, sequence_of_strings):
        self.base_seq = sequence_of_strings
        self.count = 0
        self.max = len(self.base_seq)

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max:
            count = self.count
            self.count += 1
            spam = "spam, " * self.count
            return spam + "and " + self.base_seq[count]
        else:
            raise StopIteration()

for value in MyIterator(dogs):
    print(value)
