#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """initiate the __size attribute
        verify if size is an integer
        verify if size is less than 0
        
        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate the area of the square

        return:
            area of the square
        """
        return pow(self.__size, 2)

    @property
    def size(self):
        """retrive the size of the square

        return:
            size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square

        Args:
            value (int): the value to set the size to
        """
        self.__size = value
