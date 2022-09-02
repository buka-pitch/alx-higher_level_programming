#!usr/bin/python3
def square_matrix_simple(matrix):
    """ function to sqare the value of each item in the matrix"""
    return [[i**2 for i in row] for row in matrix]
