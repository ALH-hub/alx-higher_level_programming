#!/usr/bin/python3
"""define the to_json_string function"""
import json


def to_json_string(my_obj):
    """the json representation of an object
    Args:
        my_obj (object): object concerned
    Returns:
        JSON representation of the object
    """
    return json.dumps(my_obj)
