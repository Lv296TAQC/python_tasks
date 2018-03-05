""""This module solves the task 108."""


def func2(number):
    """"
    Take a natural number and return the smallest number looks like 2**degree,
    which is bigger than entered number.

    Args:
        number (int): any natural number

    Returns:
        result (int): the smallest number 2**r bigger than entered number

    """
    degree = 1
    while 2**degree <= number:
        degree += 1
    result = 2**degree
    return result
