""""This module solves the task 108."""


def func2(number: int) -> int:
    """
    Take a natural number and return the smallest number looks like 2**degree,
    which is bigger than entered number.

    :param number: Any natural number.
    :return result: The smallest number 2**r bigger than entered number.

    >>> func2(69)
    128
    """
    degree = 1
    while 2**degree <= number:
        degree += 1
    result = 2**degree
    return result
