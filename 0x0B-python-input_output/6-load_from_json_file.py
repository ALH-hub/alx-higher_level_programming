#!/usr/bin/python3
"""define load_from_json_file function"""
import json


def load_from_json_file(filename):
    """load the json string from a json file
    Args:
        filename (string): json file name
    Returns:
        the object representation of the json file content
    """
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    return json.loads(text)