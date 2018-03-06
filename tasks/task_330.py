# -*- coding: utf-8 -*-
"""This module solves the task 330 from zadachi.pd"""
from tasks.task_227 import divisor


def minus_last(num: int) -> int:
    """
    the sum of all the divisors except itself
    :param num: int numbers
    :return:  int sum of all the divisors except itself (num)
    """
    sum_div = 0
    list_minus = divisor(num)
    list_minus.remove(num)
    for i in list_minus:
        sum_div = sum_div + i
    return sum_div


def ideal(limit: int) -> list:
    """

    finds perfect numbers
    :param limit: int number
    :return: list of  perfect numbers which are less than limit
    """
    ideal_list = []

    for i in range(1, limit):

        if i == minus_last(i):
            ideal_list = ideal_list + [i]
    return ideal_list
