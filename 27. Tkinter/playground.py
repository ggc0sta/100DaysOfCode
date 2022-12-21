def add(*args):  # *args allows us to use any number of arguments in a function
    my_sum = 0
    for number in args:
        my_sum += number
    return my_sum


print(add(1, 3))
print(add(1, 3, 2, 5))


def calculate(n, **kwargs):  # keyword arguments
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

