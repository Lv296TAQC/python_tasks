"""This module solves the task 87 from zadachi.pdf"""


def natural_number(n_number, m_number):
    """
    Get the sum of the last digits of the number n.

    :param n_number: any natural number
    :param m_number: any natural number
    :return: int, which return last digits of the number.

    ..doctest:
    >>>print(natural_number(21,12))
    3
    """
    counter = 0
    while m_number > 0:
        counter += n_number % 10
        n_number //= 10
        m_number -= 1
    return counter
