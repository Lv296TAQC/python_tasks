#!/usr/bin/python
"""Oleksandr's Module"""


def task323(from_input):
    """Function solves task 323 MOO."""
    result = []
    check_for_div = 0
    for try_for_result in range(2, from_input):
        for coprime in range(2, try_for_result + 1):
            if try_for_result % coprime == 0 and from_input % coprime == 0:
                check_for_div = check_for_div + 1
        if check_for_div == 0:
            result.append(try_for_result)
        check_for_div = 0
    return result
