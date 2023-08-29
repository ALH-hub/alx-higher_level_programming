#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """initiate the __size attribute

        Args:
            size (int): the size of the square
        """
        self.size = size

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
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size of the square
        verify if new size is an integer
        verify if new size is less than 0

        Args:
            value (int): the value to set the size to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """define the == comparision to a Square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """define the != comparison to a Square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """define the < comparison to a Square"""
        return self.area() < other.area()

    def __le__(self, other):
        """define the <= comparison to a Square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """define the > comparison to a Square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """define the >= compmarison to a Square"""
        return self.area() >= other.area()
