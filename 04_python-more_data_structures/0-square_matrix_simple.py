#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for element in matrix:
        square.append(list(map(lambda x: x**2, element)))
    return (square)
