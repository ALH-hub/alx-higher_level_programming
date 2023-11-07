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

    def to_json(self):
        """dictionary representation of the student"""
        return self.__dict__