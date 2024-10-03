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

    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1