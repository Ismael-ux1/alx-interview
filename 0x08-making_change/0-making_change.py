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

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1  # Cannot be met
    else:
        return dp[total]
