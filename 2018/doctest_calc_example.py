"""A simple calculator module to demo using doctest"""

from functools import reduce

def add(*args):
    """Return the sum of all arguments

    Integers can be added:
    >>> add(2, 2)
    4

    And an arbitary number of arguments can be used:
    >>> add(2, 2, 6)
    10
    """
    return sum(args)

def multiply(*args):
    """Return the produce of all arguments

    Integers can be multiplied:
    >>> multiply(3, 4)
    12

    Decimal numbers can be used:
    >>> multiply(0.4, 0.5)
    0.2

    And an arbitary number of arguments can be used:
    >>> multiply(2, 8, 4)
    64
    """
    return reduce((lambda x, y: x * y), args)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed > 0:
        exit(1)
