#!/usr/bin/python3
"""
returns the perimeter of the island described in grid:
"""
def island_perimeter(grid):
    """
    grid: A 2D list representing the island. 1s represent land, 0s represent water.
    
    Returns: The perimeter of the island.
    """
    perimeter = 0

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  

                perimeter += 4

                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2
    
    return perimeter
