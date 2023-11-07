#!/usr/bin/python3
"""defines Student class"""


class Student:
    """representation of student"""

    def __init__(self, first_name, last_name, age):
        """new student

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of the student
        Args:
            attrs (list): attributes to represent and optional
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__