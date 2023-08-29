#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """initiate the __size attribut
e
        Args:
            size (int): the size of the square
        """
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
        verify if new size is an integer
        verify if new size is less than 0

        Args:
            value (int): the value to set the size to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print a square with character #
        if size is 0, print a new line
        """
        if self.__size == 0:
            print()
        else:
            for i in range(1, self.__size + 1):
                for j in range(1, self.__size + 1):
                    print('#', end="")
                print()
