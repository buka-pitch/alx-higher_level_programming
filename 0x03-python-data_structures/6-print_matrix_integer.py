#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """function to take a matrix (nested list and print it)"""
    if matrix:
        for i in matrix:
            for j in i:
                print("{}".format(j), end=' ')
            print('{}'.format('\n'), end='')
