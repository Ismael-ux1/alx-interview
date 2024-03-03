#!/usr/bin/python3
"""
This function calculates the minimum number of coins,
needed to make a given total.
"""


def makeChange(coins, total):
    """
    This function calculates the minimum number of coins,
    needed to make a given total.
    """
    if total <= 0:
        return 0

    # Initialize the dp table
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Build the dp table
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1  # Cannot be met
    else:
        return dp[total]
