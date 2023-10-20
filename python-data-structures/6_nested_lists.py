#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()  # Start a new line after each row

print_matrix(matrix)
