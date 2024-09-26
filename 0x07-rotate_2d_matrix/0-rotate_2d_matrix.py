#!/usr/bin/env python3

"""
 rotates a matrix 90 degrees clockwise.

"""

def rotate_2d_matrix(matrix):

 """
Rotates a given n x n 2D matrix 90 degrees clockwise in place.

 Args:
        matrix (list of list of int): A 2D list representing the matrix to be rotated.
        
    Returns:
        None: The function modifies the input matrix in place.
"""

    n = len(matrix)

 for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp
