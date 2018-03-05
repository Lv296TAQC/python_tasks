#!/usr/bin/python
"""Oleksandr's module for solving task 224"""


def task224(from_input):
    """Take input natural number and search for all it's natural dividers

    Args:
        from_input (int): Incoming value

    Returns:
        result (list): Return list of all natural dividers
    """
    result = []
    for try_natural in range(1, from_input + 1):
        if from_input % try_natural == 0:
            result.append(try_natural)
    return result
