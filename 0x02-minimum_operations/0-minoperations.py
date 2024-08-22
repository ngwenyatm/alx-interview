#!/usr/bin/python3
"""
Calculates the minimum number of operations required to convert a given integer n to 1.

Parameters:

    n: The integer to be converted.

Returns:

    The minimum number of operations needed.
"""


def minOperations(n):
    if (n <= 1):
        return 0
    no_operation = 0
    fact = 2

    while (n > 1):
        if n % fact == 0:
            while (n % fact == 0):
                n = (n / fact)
                no_operation += fact
        fact += 1
    return no_operation
