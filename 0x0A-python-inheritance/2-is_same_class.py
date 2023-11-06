#!/usr/bin/python3
"""defines is_same_class function"""


def is_same_class(obj, a_class):
    """verify if an object if an instance of a class
    Args:
        obj (object): the object to check
        a_class (class): the class concerned
    Return:
        True if obj is an instance
        False otherwise
    """
    if type(obj) is a_class:
        return True

    return False
