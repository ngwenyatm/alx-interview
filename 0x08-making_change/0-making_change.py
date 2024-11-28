#!/usr/bin/python3

"""This contains the making change module/function"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make up a given amount.

    Args:
        coins (list): A list of positive integers representing coin denominations.
        total (int): The target amount to be made using the fewest coins.

    Returns:
        int: The minimum number of coins needed to make up the total.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be achieved with the given coins.
    """
    if total <= 0:
        return 0
    
    remaining_amount = total
    current_index = 0
    coin_count = 0

    sorted_coins = sorted(coins, reverse=True)
    total_coins = len(coins)
    
    while remaining_amount > 0:
        if current_index >= total_coins:
            return -1
        if remaining_amount - sorted_coins[current_index] >= 0:
            remaining_amount -= sorted_coins[current_index]
            coin_count += 1
        else:
            current_index += 1
    
    return coin_count