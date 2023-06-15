#!/usr/bin/python3
'''
Unittest for max_integer([..])
'''


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):
    def test_order(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_desorder(self):
        result = max_integer([5, 7, 2, 1, 21])
        self.assertEqual(result, 21)

    def test_negatives(self):
        result = max_integer([-2, -5, -21, -1])
        self.assertEqual(result, -1)

    def test_one(self):
        result = max_integer([21])
        self.assertEqual(result, 21)

    def test_none(self):
        result = max_integer([])
        self.assertEqual(result, None)

    if __name__ == "__main__":
        unittest.main()
