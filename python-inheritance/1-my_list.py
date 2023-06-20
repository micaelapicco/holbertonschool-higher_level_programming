#!/usr/bin/python3
""" 1-my list Module"""


class MyList(list):
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
