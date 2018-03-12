""""This module solves the task 86(b)."""


def sum_of_digits(number: int) -> int:
    """
    Take a natural number and return the sum of its digits .

    :param number: Any natural number.
    :return result: Sum of digits of entered number.

    >>> sum_of_digits(46)
    10
    """
    strn = str(number)
    result = 0
    for i in strn:
        result += int(i)
    return result
