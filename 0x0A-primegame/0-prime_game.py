#!/usr/bin/python3
""" Module for solving the prime game question """

def isWinner(x, nums):
    """
    Determines the winner of a game played between Maria and Ben.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers, where each integer represents the upper limit of the range for each round.

    Returns:
        str: "Maria" if Maria wins more rounds, "Ben" if Ben wins more rounds, or None if it is a tie.
    """
    if x < 1 or not nums:
        return None

    max_value = max(nums)
    prime_flags = [True] * (max_value + 1)
    prime_flags[0] = prime_flags[1] = False

    for num in range(2, int(max_value**0.5) + 1):
        if prime_flags[num]:
            for multiple in range(num * num, max_value + 1, num):
                prime_flags[multiple] = False

    prime_counts = [0] * (max_value + 1)
    for num in range(1, max_value + 1):
        prime_counts[num] = prime_counts[num - 1] + (1 if prime_flags[num] else 0)

    maria_score = 0
    ben_score = 0

    for n in nums:
        total_moves = prime_counts[n]
        if total_moves % 2 == 1:
            maria_score += 1
        else:
            ben_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None


