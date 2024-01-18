#!/usr/bin/env python3
""" Calculate the minimum number of operations to get n 'H's. """


def minOperations(n):
    """
    Args:
    - n (int): The target number of 'H's.

    Returns:
    - int: The minimum number of operations to get n 'H's.
    """

    # Base case: if n is 1, no operations are needed.
    if n == 1:
        return 0
    # For each number of i from n//2 down to 1...
    for i in range(n//2, 0, -1):
        # If n is divisible by i.
        if n % i == 0:
            #  Recursively solve the problem for i, and add the of,
            # operations needed to reach n from i by pasting.
            return minOperations(i) + n // i
        # If no i is found such that n is divisible by i, return 0.
        # This means that n is impossible to achive.
        return 0
