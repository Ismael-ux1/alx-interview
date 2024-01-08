#!/usr/bin/python3
"""A function that returns pascal triangle"""


def pascal_triangle(n):
    """ Returns an empty list if n <= 0 """
    if n <= 0:
        return []

    # Creates a list of lists to store the triangle
    triangle = [[1]]

    # Loops through each row of the triangle
    for i in range(1, n):

        # Creates a list to store the current row
        row = [1]

        # Loops through each element of the current row,
        # except the first and last one
        for j in range(1, i):

            # Calculates the value of the current element
            # as the sum of the two elements above it
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            # Appends the value to the current row
            row.append(value)
        # Appends 1 to the end of the current row
        row.append(1)
        # Appends the current row to the triangle
        triangle.append(row)
    # Returns the triangle
    return triangle
