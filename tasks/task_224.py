#!/usr/bin/python
"""Oleksandr's module for solving task 224"""


def task224(from_input: int) -> list:
    """
    Take input natural number and search for all it's natural dividers.

    :param int from_input: Incoming value.
    :return list result: Return list of all natural dividers.
    """
    result = []
    for try_natural in range(1, from_input + 1):
        if from_input % try_natural == 0:
            result.append(try_natural)
    return result
