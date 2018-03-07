"""This module solves the task 178b from zadachi.pdf"""


def multiple_numbers(list_of_numbers):
    """
    Determine the number of numbers that are multiples of 3 and not multiple 5

    :param list_of_numbers: list of natural number
    :return: int, which return count of list_of_n_numbers

    ..doctest:

    >>>print(multiple_numbers([15]))
    3
    """
    counter = 0
    for i in list_of_numbers:
        if i % 3 == 0 and i % 5 == 1:
            counter += 1
    return counter
