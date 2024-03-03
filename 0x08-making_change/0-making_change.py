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

    memo = {}

    def dp(target):
        if target < 0:
            return float('inf')
        if target == 0:
            return 0
        if target in memo:
            return memo[target]

        min_coins = float('inf')
        for coin in coins:
            min_coins = min(min_coins, dp(target - coin) + 1)

        memo[target] = min_coins
        return min_coins

    result = dp(total)

    return result if result != float('inf') else -1
