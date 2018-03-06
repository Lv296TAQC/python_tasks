#!/usr/bin/python
"""Oleksandr's module for solving task 88a"""


def task88a(from_input: int) -> bool:
    """
    Take input value and raise it to the power of 2.
    Return True if there is '3' in 'check' variable.
    Return False if there is '3' in 'check' variable.

    :param int from_input: Incoming value.
    :return bool: True if there is digit 3 in powered input value,
        False if there is no digit 3 in powered input value.
    """
    from_input = from_input ** 2
    for check in str(from_input):
        if check == '3':
            return True
    return False
