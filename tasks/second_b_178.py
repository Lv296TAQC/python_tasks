# -*- coding: utf-8 -*-
"""This module solves the task 178b from zadachi.pd"""
import math


def count_sq(posl):
    """
    count the number is the square root  of a even number
    arg:
        posl list contains numbers

    return:
        count of the number which is a square root of a even number

    """
    posl = list(posl)
    addposl = []
    poslsq = []
    for k in posl:
        if k % 2 == 0:
            addposl = addposl + [k]  # вибираємо парні бо квадрат парного парне
    for j in addposl:
        if math.sqrt(j) % 2 == 0:  # чи корінь є парним
            poslsq = poslsq + [j]
    return len(poslsq)


#print count_sq([1, 5, 100, 9, 36, 16])
