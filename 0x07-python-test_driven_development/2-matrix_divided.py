#!/usr/bin/python3
''' Module doc '''


def matrix_divided(matrix, div):
    '''
        divides a matrix value by a divisor
    '''
    new_matrix = []
    length = len(matrix[0])
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(err)
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err)
            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
