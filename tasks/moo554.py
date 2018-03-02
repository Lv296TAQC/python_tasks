#!/usr/bin/python
"""Oleksandr's module for solving task 554"""


def task554(from_input):
    """Take input natural number and search for all it's Pythagorean triples,
    that like 'a < b < c < input natural number'

    Args:
        from_input (int): Incoming value

    Returns:
        result (dict): Return dict with all Pythagorean triples
    """
    key = 1
    result = {}
    for c_pifagor in range(from_input):
        for b_pifagor in range(c_pifagor):
            for a_pifagor in range(b_pifagor):
                if c_pifagor ** 2 == a_pifagor ** 2 + b_pifagor ** 2:
                    result[key] = [a_pifagor, b_pifagor, c_pifagor]
                    key += 1
    return result
