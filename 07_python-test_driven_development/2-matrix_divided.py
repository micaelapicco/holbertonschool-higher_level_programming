#!/usr/bin/python3
'''
Task 2: Write a function that divides all elements of a matrix.
'''


def matrix_divided(matrix, div):
    """Errors cases"""
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    for array in matrix:
        for element in array:
            if type(element) != int and type(element) != float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")
    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    for element in matrix:
        new.append(list(map(lambda x: round((x / div), 2), element)))
    return (new)
