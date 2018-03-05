"""This module solves the task 178e from zadachi.pdf"""
from math import factorial


def func(arr):
    """
    Count the elements satisfying the condition: (2^k < ak < k!).

    Arg:
        arr (list): contains numbers.

    Return:
        count (int): number appropriate elements.

    Example:
        >>> print(func([0, 0, 1, 6, 23, 33])
        2
    """
    count = 0
    for index, elem in enumerate(arr):
        if pow(2, index) < elem < factorial(index):
            count += 1
    return count
