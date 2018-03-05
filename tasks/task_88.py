# -*- coding: utf-8 -*-
"""This module solves the task 88a from zadachi.pd"""


def three_go_in(numb):
    """
    checks for the entry of 3 to the square of the number
    arg:
        numb:any number
    return:
        True if 3 entry to the square of the number
        False if 3 not entry to the square of the number
    """
    numb_sq = numb ** 2
    numb_sq = str(numb_sq)
    if (numb_sq.find('3')) >= 0:  # return -1 if not and if there is a position.
        return True
    return False
