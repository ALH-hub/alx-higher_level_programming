#!/usr/bin/python3
"""defines the read_file function"""


def read_file(filename=""):
    """read a file and print the content to stdout
    Args:
        filename (file): file name to read
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
