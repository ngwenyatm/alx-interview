#!/usr/bin/python3

"""
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total
"""

def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    
    remaining_amount = total
    coin_count = 0
    current_index = 0
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