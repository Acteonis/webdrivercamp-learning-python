#!/usr/bin/python3

def compute_matrix(matrix=[]):
    return [list(map(lambda x: x ** 2, row)) for row in matrix]

if __name__ == "__main__":
    matrix = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    print(f"Original: {matrix}")
    modified_matrix = compute_matrix(matrix)
    print(f"Modified: {modified_matrix}")
