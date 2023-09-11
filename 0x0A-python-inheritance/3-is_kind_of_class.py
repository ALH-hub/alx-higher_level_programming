#!/usr/bin/python3
"""defines the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of or if object
        is an instance of a class that inherited from
    Args:
        obj (object): object of a class
        a_class (class): class
    Return:
        True if object is an instance or
            if object is an instance of a class inherited from
        False otherwise
    """
    if isinstance(obj,  a_class) or issubclass(type(obj), a_class):
        return True
    return False
