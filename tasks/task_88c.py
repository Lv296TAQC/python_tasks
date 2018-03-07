"""This module solves the task 88c from zadachi.pdf"""
from math import log10


def swap_numb(numb: int) -> int:
    """
    Swap the first and the last digits of the number.

    :param numb: any number.
    :return: where the first and the last digits are swapped.

    :Example:
        >>> swap_numb(1356)
        6351
    """
    rank = pow(10, int(log10(numb)))
    first = numb // rank
    last = numb % 10
    return numb - (first - last) * rank - last + first
