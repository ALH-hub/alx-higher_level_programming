#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """empty Square class"""
    def __init__(self, size=0):
        """initiate the __size attribute
        verify if size provided is and integer
        verify if size provided is less than 0

        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
