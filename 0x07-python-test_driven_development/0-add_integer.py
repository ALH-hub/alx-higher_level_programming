#!/usr/bin/python3
"""addidition function of integers"""


def add_integer(a, b=98):
    """returns the integer addition of two numbers

    Adds two numbers provided to the function

    Raises:
        TypeError: if either of the parameters are non-int or non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))