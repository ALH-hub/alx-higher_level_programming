#!/usr/bin/python3
"""defines the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """save a json string representation to a file
    Args:
        my_obj (object): object to serialize
        filename (string): the file name to save to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)