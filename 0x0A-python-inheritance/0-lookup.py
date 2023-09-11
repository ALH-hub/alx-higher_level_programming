#!/usr/bin/python3

"""define the lookup function"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    attribute = []
    method = []

    for item in dir(obj):
        if not item.startswith('__'):
            if callable(getattr(obj, item)):
                method.append(item)
            else:
                attribute.append(item)

    return attribute + method
