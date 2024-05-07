#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given number recursively.

    Parameters:
    n (int): The number for which factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Command-line argument for the number whose factorial needs to be calculated
f = factorial(int(sys.argv[1]))
print(f)