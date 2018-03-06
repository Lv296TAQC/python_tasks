# -*- coding: utf-8 -*-
"""This module solves the task 560 from zadachi.pd"""
from tasks.task_330 import minus_last


def amicable() -> list:
    """
    Finds all amicable numbers  for a range of 200-300
    :return: list with pairs amicable numbers
    """
    amica_list = []
    level_up = 0
    for k in range(200, 300):
        level_up = level_up + 1
        for j in range(200 + level_up, 300):
            if minus_last(k) == j:
                if minus_last(j) == k:
                    amica_list = (amica_list) + [(k, j)]
    return amica_list
