#!/usr/bin/python3

"""
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total
"""

def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet a given total amount.

    Args:
        coins: A list of ints as the denominations of coins.
        total: The amount to be met.

    Returns:
        The fewest number of coins needed to meet the total amount, or else returns -1.
    """
    if total == 0:
        return 0
    dp = {0: 0}  # Initialize DP table with base case
    for coin in coins:
        for i in range(coin, total + 1):
            if i in dp:
                dp[i] = min(dp[i], dp[i - coin] + 1)
            else:
                dp[i] = float('inf')
    return dp[total] if dp[total] != float('inf') else -1