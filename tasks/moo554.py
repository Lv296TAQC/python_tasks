#!/usr/bin/python
"""Oleksandr's Module"""


def task554(from_input):
    """Function solves task 554 MOO."""
    key = 1
    result = {}
    for c_pifagor in range(from_input):
        for b_pifagor in range(c_pifagor):
            for a_pifagor in range(b_pifagor):
                if c_pifagor ** 2 == a_pifagor ** 2 + b_pifagor ** 2:
                    result[key] = [a_pifagor, b_pifagor, c_pifagor]
                    key += 1
    return result
