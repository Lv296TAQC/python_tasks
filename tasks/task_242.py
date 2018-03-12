"""Calculate the expression. Solves task 242 from zadachi.pdf"""

import math


def total_sum(number_n: int) -> int:
    """
    Method for calculating the total sum in the range

    :param: Natural validated number from Input
    :return: sum from k to n of the expression

    Example:

    ..doctest::

        >>>print(total_sum(2))
        1.5
    """
    sum1 = 0
    for k in range(number_n+1):
        formula = ((-1) ** (k * (k - 1) * 0.5)) / math.factorial(k)
        sum1 += formula
    return sum1
