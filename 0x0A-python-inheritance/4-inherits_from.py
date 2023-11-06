#!/usr/bin/python3
"""defines the function inherits_from"""


def inherits_from(obj, a_class):
    """check the inheritance of an object
    Args:
        obj (object): the object of a class
        a_class (class): the class
    Return:
        True if object is an instance of a
        class inherited from a specific class
        False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
