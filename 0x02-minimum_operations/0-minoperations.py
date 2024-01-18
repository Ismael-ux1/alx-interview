#!/usr/bin/python3
""" Calculate the minimum number of operations to get n 'H's. """


def minOperations(n):
    """
    Args:
    - n (int): The target number of 'H's.

    Returns:
    - int: The minimum number of operations to get n 'H's.
    """

    # If n is less than or equal to 0,
    # return 0 as it's impossible to have 'H' characters
    if n <= 1:
        return 0
    # Initialize the result to 0
    res = 0

    # Initialize the divisor to 2
    p = 2

    # Loop until n is greater than 1
    while n > 1:
        # While n is divisible by p
        while n % p == 0:

            # Add p to the result
            res += p
            # Divide n by p.
            n //= p
        # Increament p by 1
        p += 1
    # Return the result
    return res
