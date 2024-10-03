#!/usr/bin/python3

def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet a given total amount.

    Args:
        coins: A list of ints as the denominations of coins.
        total: The amount to be met.

    Returns:
        The fewest number of coins needed to meet the total amount, or else returns -1.
    """

    if not coins or total <= 0:
        return 0 if total == 0 else -1

    coins.sort(reverse=True)

    change = 0
    while total > 0:
        if not coins or total < coins[0]:
            return -1
        coin = coins[0]
        change += total // coin
        total %= coin

    return change