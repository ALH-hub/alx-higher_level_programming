#!/usr/bin/python3
"""max integer function"""


def max_integer(list=[]):
    """returns the max integer from a list
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

