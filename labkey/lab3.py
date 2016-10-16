# Without modifying the internals either function, can
# you code a solution to wait 1 second between verses?
# hint on the import below

from time import sleep

def sleeper(some_function):
    def wrapper(number):
        some_function(number)
        sleep(1)
    return wrapper

@sleeper
def bottles_of_beer(number):
    print("{number} bottles of craft beer on the wall, {number} bottles of craft beer".format(number=number))
    print("Take one down, pass it around")
    print("{} bottles of craft beer on the wall".format(number-1))
    print("")


def bottles_of_beer_game(start_bottles=100):
    for count in range(start_bottles, 0, -1):
        bottles_of_beer(count)


bottles_of_beer_game(10)