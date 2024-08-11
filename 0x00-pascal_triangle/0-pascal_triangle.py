#!/usr/bin/python3
  """Returns a list of lists representing Pascal's triangle of n rows.
  """
def pascal_triangle(n):
  """Returns n rows of Pascal's triangle."""

  if n <= 0:
    return []

  pascal_triangle = []
  for row_num in range(n):
    row = [1] * (row_num + 1)
    for col_num in range(1, row_num):
      row[col_num] = pascal_triangle[row_num - 1][col_num - 1] + pascal_triangle[row_num - 1][col_num]
    pascal_triangle.append(row)

  return pascal_triangle
