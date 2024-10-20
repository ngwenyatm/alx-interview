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
    
    if not nums or x < 1:
        return None
    
    max_num = max(nums)

    prime_filter = [True for _ in range(max(max_num + 1, 2))]
    
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not prime_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            prime_filter[j] = False
    
    prime_filter[0] = prime_filter[1] = False
    
    prime_count = 0
    for i in range(len(prime_filter)):
        if prime_filter[i]:
            prime_count += 1
        prime_filter[i] = prime_count

    maria_wins = 0
    
    for num in nums:
        if prime_filter[num] % 2 == 1:
            maria_wins += 1
    
    if maria_wins * 2 == len(nums):
        return None
    elif maria_wins * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"

