#!/usr/bin/python3
"""defines the from_json_string function"""
import json


def from_json_string(my_str):
    """convert from string to python object
    Args:
        my_str (string): string concerned
    Returns:
        object represented by the json string
    """
    return json.loads(my_str)
