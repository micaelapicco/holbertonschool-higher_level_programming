#!/usr/bin/python3
""""
Task 12: Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Return a last of list of int representing the Pascal Triangle"""
    triangle = [[1]]
    for h in range(n - 1):
        new = []
        for lst in range(len(triangle[h]) + 1):
            if lst == 0 or lst == len(triangle[h]):
                new.append(1)
            else:
                new.append(triangle[h][lst - 1] + triangle[h][lst])
        triangle.append(new)
    return triangle
