#!/usr/bin/python
"""Oleksandr's Module"""


def task224(from_input):
    """Function solves task 224 MOO."""
    result = []
    for try_natural in range(1, from_input + 1):
        if from_input % try_natural == 0:
            result.append(try_natural)
    return result
