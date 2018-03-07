"""This module solves the task 329 from zadachi.pdf"""


def sum_of_digits(number):
    """
    Return the sum of digits of entered number

    :param number: any natural number
    :return: int, where return sum of the digits

    ..doctest:
    >>>print(sum_of_digits(345))
    12
    """
    translate_var = str(number)
    result_integer = 0
    for i in translate_var:
        result_integer += int(i)
    return result_integer


def main_func(n_number, m_number):
    """
     Get all smaller and natural numbers, the square of the sum of the digits of which is equal to m.

    :param n_number: any natural number
    :param m_number: any natural number
    :return: list, where the numbers returned, the sum of digits equal to m.

    ..doctest:
    >>>print(main_func(45, 21))
    []
    """
    counter_list = []
    for i in range(n_number):
        if pow(sum_of_digits(i), 2) == m_number:
            counter_list.append(i)
    return counter_list
