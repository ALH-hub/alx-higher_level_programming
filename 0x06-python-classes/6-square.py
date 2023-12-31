#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initiate the __size attribut
e
        Args:
            size (int): the size of the square
            position (int, int): the position of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """get the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print square with the # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
