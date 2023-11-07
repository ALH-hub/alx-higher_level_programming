#!/usr/bin/python3
"""define the appen_write function"""


def append_write(filename="", text=""):
    """appends a given text to a file
    Args:
        filename (string): the file name concerned
        text (string): the characters to append
    Returns:
        number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))