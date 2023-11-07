#!/usr/bin/python3
"""defines class_to_json function"""


def class_to_json(obj):
    """returns dict representation of a class"""
    return obj.__dict__
