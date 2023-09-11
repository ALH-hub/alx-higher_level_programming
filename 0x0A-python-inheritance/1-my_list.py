#!/usr/bin/python3

"""defines the print_sorted class"""


class MyList(list):
    """list class to print in ascending order"""
    def print_sorted(self):
        """print a list in sorted order"""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
