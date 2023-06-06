#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elemnt in row:
            print("{:d}".format(element), end="")
