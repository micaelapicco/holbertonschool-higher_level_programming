#!/usr/bin/python3
'''
Task 4: Write a function that prints a square with the character #.
'''


def print_square(size):
    """Print square of size x"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("{}".format("#" * size))
