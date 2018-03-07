"""This module solves the task 226 from zadachi.pdf"""


def common_multiple(n_number, m_number):
    """
    Get all their natural common multiples, smaller mn

    :param n_number: any natural number
    :param m_number: any natural number
    :return: list, which returns common multiples, smaller mn

    ..doctest:
    >>>print(common_multiple(32,2))
    [32]
    """

    counter = []
    for i in range(1, m_number * n_number):
        if i % m_number == 0 and i % n_number == 0:
            counter.append(i)
    return counter
