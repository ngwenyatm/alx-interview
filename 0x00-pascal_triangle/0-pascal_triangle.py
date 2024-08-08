#!/usr/bin/python3
  """Returns a list of lists representing Pascal's triangle of n rows.
  """

def pascal_triangle(n):
    # If input n <= 0, return empty list
    if n <= 0:
        return []

    # Initialize list to hold the triangle
    Ptriangle = []

    # generate each row of the triangle
    for i in range(n):
        # Start current row with 1s
        row = [1] * (i + 1)
        
        # fill the current row with sum of elements in the previous row
        for j in range(1, i):
            row[j] = Ptriangle[i-1][j-1] + Ptriangle[i-1][j]
        
        # Add current row to triangle
        Ptriangle.append(row)

    # Return the completed triangle
    return Ptriangle
