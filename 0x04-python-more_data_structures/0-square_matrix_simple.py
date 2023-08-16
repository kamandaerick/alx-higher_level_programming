#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in matrix:
        squared_row = []
        for j in i:
            squared_row.append(j ** 2)
        result.append(squared_row)
    return result
