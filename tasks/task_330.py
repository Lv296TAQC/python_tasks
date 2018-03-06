# -*- coding: utf-8 -*-
"""This module solves the task 330 from zadachi.pd"""
from tasks.task_227 import divisor


def minus_last(num):
    """
    the sum of all the divisors except itself
    arg:
    num init numbers

    return:
    int sum of all the divisors except itself (num)

           """
    sum_div = 0
    list_minus = divisor(num)
    list_minus.remove(num)
    for i in list_minus:
        sum_div = sum_div + i
    return sum_div


def ideal(limit):
    """
        finds perfect numbers
         perfect number is a positive integer that is equal to the sum\n
         of its proper positive divisors, that is, the\n
         sum of its positive divisors excluding the number itself
        arg:
        limit init numbers

        return:
        list of  perfect numbers which are less than limit

               """
    ideal_list = []

    for i in range(1, limit):

        if i == minus_last(i):
            ideal_list = ideal_list + [i]
    return ideal_list


#print(ideal(False))
