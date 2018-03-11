"""Calculate the expression. Solves task 242 from zadachi.pdf"""

import math


def total_sum(number_n):
    """
    Method for calculating the total sum in the range

    Arg:
        natural number n
    Return:
        sum from k to n of the expression
    Example:
        print(total_sum(2)) --> 1.5
    """
    sum1 = 0
    for k in range(number_n+1):
        formula = ((-1) ** (k * (k - 1) * 0.5)) / math.factorial(k)
        sum1 += formula
    return sum1
