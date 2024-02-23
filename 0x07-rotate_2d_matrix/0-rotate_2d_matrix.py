#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix: list) -> None:
    """ This function takes a list as an input and returns nothing """
    # Get the size of the matrix
    n = len(matrix)
    # Iterate over each layer of the matrix
    for i in range(n // 2):
        # Iterate over each element in the current layer
        for j in range(i, n - i - 1):
            # Store the top-left element in a temporary variable
            temp = matrix[i][j]
            # Move the bottom-left element to the top-left position
            matrix[i][j] = matrix[n - 1 - j][i]
            # Move the bottom-right element to the bottom-left position
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            # Move the top-right element to the bottom-right position
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            # Move the temporary variable to the top-right position
            matrix[j][n - 1 - i] = temp
