""""This module solves the task 86(b)."""


def sum_of_digits(number):
    """"
    Take a natural number and return the sum of its digits .

    Args:
        number (int): any natural number

    Returns:
        result (int): sum of digits of entered number

    """
    strn = str(number)
    result = 0
    for i in strn:
        result += int(i)
    return result
