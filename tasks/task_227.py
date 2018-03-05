# -*- coding: utf-8 -*-
"""This module solves the task 227 from zadachi.pd"""


def divisor(num):
    """
       finds divisor of the number
       arg:
           num init numbers

       return:
              list with divisor of the number

       """
    list_div = []
    for i in range(1, num + 1):
        if num % i == 0:
            list_div = list_div + [i]
    return list_div


def comparison(number_1, number_2):
    """
          finds   divisor of the two nambers(negative and positive)
          arg:
              number_1,number_2 init numbers

          return:
                 list with common divisors two numbers(number_1,number_2)

          """
    list_sp_div = []

    for j in divisor(number_1):
        for k in divisor(number_2):
            if j == k:
                list_sp_div = list_sp_div + [j]
    for i in list_sp_div:                       #цикл для доповнення відємними числами
        minus = -i
        list_sp_div = [minus] + list_sp_div
    return list_sp_div


#print comparison(6, 36)
