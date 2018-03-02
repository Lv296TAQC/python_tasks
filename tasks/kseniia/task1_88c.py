"""This module solves the task 88c from zadachi.pdf"""
from math import log10


def swap_numb(numb):
    """
    Swap the first and the last digits of the number.

    Arg:
        numb (int): any number.

    Return:
        int, where the first and the last digits are swapped.
    """
    rank = pow(10, int(log10(numb)))
    first = numb // rank
    last = numb % 10
    return numb - (first - last) * rank - last + first


print(swap_numb(1356))
