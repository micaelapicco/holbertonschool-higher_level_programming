#!/usr/bin/python3
'''
Unittest for max_integer([..])
'''


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):
    def test_order(self):
        """max value at the end"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_desorder(self):
        """max value at the middle"""
        result = max_integer([5, 7, 21, 2, 1])
        self.assertEqual(result, 21)

    def test_desorder(self):
        """max value at the beginning"""
        result = max_integer([21, 7, 9, 2, 1])
        self.assertEqual(result, 21)

    def test_negatives(self):
        """all values negatives"""
        result = max_integer([-2, -5, -21, -1])
        self.assertEqual(result, -1)

    def test_negatives(self):
        """some values negatives and some positives"""
        result = max_integer([-2, 5, -21, 1])
        self.assertEqual(result, 5)

    def test_one(self):
        """one value"""
        result = max_integer([21])
        self.assertEqual(result, 21)

    def test_none(self):
        """Empty list"""
        result = max_integer([])
        self.assertEqual(result, None)

    if __name__ == "__main__":
        unittest.main()
