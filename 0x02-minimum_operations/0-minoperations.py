#!/usr/bin/python3
"""
calculates the fewest number of operations needed to
result in n number of H characters 
"""

def minOperationsDP(n):
    dp_table = [0] * (n + 1)
    for i in range(2, n + 1):
        dp_table[i] = dp_table[i - 1] + 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                dp_table[i] = min(dp_table[i], dp_table[i // j] + j)
    return dp_table[n]
