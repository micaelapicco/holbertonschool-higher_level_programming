#!/usr/bin/python3
"""
Task 1: Write a class MyList that inherits from list
"""


class MyList(list):
    """My list class"""

    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
