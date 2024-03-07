#!/usr/bin/python3
"""A function that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """
    A function that returns the perimeter of the island described in grid.
    """
    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the result to 0
    result = 0

    # Iterate over each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is land (1)
            if grid[r][c] == 1:
                # Check the cell above. If it's out of bounds or water (0),
                # add 1 to the perimeter
                if r == 0 or grid[r-1][c] == 0:
                    result += 1
                # Check the cell below. If it's out of bounds or water (0),
                # add 1 to the perimeter
                if r == rows-1 or grid[r+1][c] == 0:
                    result += 1
                # Check the cell to the left.
                # If it's out of bounds or water (0), add 1 to the perimeter
                if c == 0 or grid[r][c-1] == 0:
                    result += 1
                # Check the cell to the right.
                # If it's out of bounds or water (0), add 1 to the perimeter
                if c == cols-1 or grid[r][c+1] == 0:
                    result += 1

    # Return the total perimeter
    return result
