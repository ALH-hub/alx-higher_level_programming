#!/usr/bin/python3
"""square printing"""


def print_square(size):
    """print a square with char #

    Args:
        size (int): height and width of square
    Raises:
        TypeError: if size is non-integer
        ValueError: size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

