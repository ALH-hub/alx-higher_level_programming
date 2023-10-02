#!/usr/bin/python3
"""function to add attribute to obj"""


def add_attribute(obj, atr, val):
    """add attribute if possible
    Args:
        obj (any): obj to add attribute to
        atr (str): name of new attribute
        val (any): value of attribute
    Raises:
        TypeError: if attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, val)
