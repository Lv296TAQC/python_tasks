#!/usr/bin/python
"""Oleksandr's module for solving task 107"""


def task107(from_input):
    """Take input value and search for the largest raise power value
    'quad_max' for digit 4, so after powering it is < incoming value.

    Args:
        from_input (int): Incoming value.

    Returns:
        result (int): Return biggest raise power value,
        so after powering 4 it will be < incoming value.
    """
    checker = 4
    result = 1
    for quad_max in range(from_input + 1):
        if checker ** quad_max < from_input:
            result = quad_max
    return result
