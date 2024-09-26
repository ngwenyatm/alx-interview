#!/usr/bin/env python3

"""
 rotates a matrix 90 degrees clockwise.

"""


def rotate_2d_matrix(matrix):

    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): A 2D list representing the matrix to be rotated.

    Raises:
        ValueError: If the matrix is not square or empty.

    Returns:
        None: The function modifies the input matrix in place.
    """

    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square and non-empty.")
    
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        matrix[i].reverse()
