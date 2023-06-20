#!/usr/bin/python3
""" 1-my list Module"""


class MyList(list):
    """My list class"""

    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
