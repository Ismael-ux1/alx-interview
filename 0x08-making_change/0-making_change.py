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

    # Iterate through coin denominations
    for coin in coins:

        # Build the dp table
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
        # Check if total can met by any number of coin
        if dp[total] == float('inf'):
            return -1
        else:
            return dp[total]
