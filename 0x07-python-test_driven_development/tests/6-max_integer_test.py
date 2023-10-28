#!/usr/bin/python3
"""unit test for max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """test ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """test unordered list of integers"""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """test list with a beginning"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """test empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """list with single element"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """test list of float"""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """test listints and floats"""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """test string"""
        string = "Oumate"
        self.assertEqual(max_integer(string), 'u')

    def test_empty_string(self):
        """test empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()

