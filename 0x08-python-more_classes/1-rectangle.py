#!/usr/bin/python3

"""class of rectangle"""


class Rectangle:
    """representing a recangle"""
    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """reset the width of the recangle"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """reset the height of the recangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
