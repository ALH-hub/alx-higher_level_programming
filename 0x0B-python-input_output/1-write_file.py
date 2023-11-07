#!/usr/bin/python3
"""define teh write file function"""


def write_file(filename="", text=""):
    """open a file and write the text provided
    Args:
        filename (file): the file to write to
        text (string): the characters to write to the file
    Returns:
        Number of characters written
    """
    count = 0
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)

    return count
