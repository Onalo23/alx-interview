#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.
    """
    for j in range(int(len(matrix) / 2)):
        for k in range(j, (len(matrix) - j - 1)):
            x = (len(matrix) - 1 - k)
            tmp = matrix[j][k]
            matrix[j][k] = matrix[x][j]
            matrix[x][j] = matrix[(len(matrix) - j - 1)][x]
            matrix[(len(matrix) - j - 1)][x] = matrix[k][(len(matrix) - j - 1)]
            matrix[k][(len(matrix) - j - 1)] = tmp