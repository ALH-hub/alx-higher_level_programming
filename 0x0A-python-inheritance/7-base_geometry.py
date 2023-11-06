#!/usr/bin/python3
"""defines BaseGeometry class"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """not implemented class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer parameter

        Args:
            name (str): name of parameter
            value (int): parameter to validate
        Raises:
            TypeError: if value not int
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
