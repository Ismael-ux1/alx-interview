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

    def dp(target, memo):
        if target < 0:
            return float('inf')
        if target == 0:
            return 0
        if memo[target] != -1:
            return memo[target]

        min_coins = float('inf')
        for coin in coins:
            if coin <= target:
                min_coins = min(min_coins, dp(target - coin, memo) + 1)

        memo[target] = min_coins
        return min_coins

    memo = [-1] * (total + 1)
    result = dp(total, memo)

    return result if result != float('inf') else -1
