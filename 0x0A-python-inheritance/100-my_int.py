#!/usr/bin/python3
"""class MyInt inherit from int"""


class MyInt(int):
    """invert operators == and !="""

    def __eq__(self, val):
        """overide == operator with !="""
        return self.real != val

    def __ne__(self, val):
        """overide != operator with =="""
        return self.real == val
