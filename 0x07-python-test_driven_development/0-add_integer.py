#!/usr/bin/python3
"""add two numbers of types either int or float"""

def add_integer(a, b=98):
    """defining the function to add the integers/float
    Returns:
        integer addition of two numbers
    Raises:
        TypeError: if none of the numbers are int or float type
    """

    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
        return
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
        return

    return (int(a) + int(b))
