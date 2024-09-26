#!/usr/bin/env python3

"""
Rotates a given n x n 2D matrix 90 degrees clockwise in place.

 Args:
        matrix (list of list of int): A 2D list representing the matrix to be rotated.
        
    Returns:
        None: The function modifies the input matrix in place.
"""

def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
