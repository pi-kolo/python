import math
from inspect import getfullargspec


class Overload:
    functions = {}

    def __init__(self, f):
        self.name = f.__name__
        Overload.functions[(f.__name__, len(getfullargspec(f).args))] = f

    def __call__(self, *args):
        return Overload.functions[(self.name, len(args))](*args)
        


def overload(f):
    return Overload(f)


@overload
def norm(x,y):
    return math.sqrt(x*x + y*y) 

@overload
def norm(x,y,z):
    return abs(x) + abs(y) + abs(z)

@overload
def norma(x,y):
    return 2*math.sqrt((x*x + y*y)) 

@overload
def norma(x,y,z):
    return 3*(abs(x) + abs(y) + abs(z))


print(f"norm(2,4) = {norm(2,4)}")

print(f"norm(2,3,4) = {norm(2,3,4)}")

print(f"norma(2,4) = {norma(2,4)}")

print(f"norma(2,3,4) = {norma(2,3,4)}")
