"""The Iteraable and Iterator protocols"""

dogs = ['husky', 'beagle', 'doberman', 'dachsund', 'collie', 'mutt']

# A for loop over an iterarable sequence is basically
# syntactic sugar for the following.

# When sequences are iterable they have an __iter__ method.
# Calling it produces an iterator object that wraps the list.

iterable_one = dogs.__iter__()

# or you can use the iter() built-in

iterable_two = iter(dogs)

print(type(iterable_one))  # outputs <class 'list_iterator'>

print("")

print(type(iterable_two))  # outputs <class 'list_iterator'>

print("")

# iterators have a method .next() that returns the next item
print(iterable_one.__next__())  # outputs husky

print("")

# or you can call the next() built-in

print(next(iterable_one))   # outputs beagle

print("")

while True:     # run forever unless exception
    print(next(iterable_one))  # print remaing items then raise StopIteration
