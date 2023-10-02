#!/usr/bin/python3
"""locked class"""


class LockedClass:
    """
    dont allow creation of new instances except for first_name
    """
    __slots__ = ["first_name"]
