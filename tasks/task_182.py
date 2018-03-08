"""Find quantity and sum of some numbers in given length sequence"""

import random

from tasks.task_88d import is_natural


def sum_div5_notdiv7(list_: list) -> tuple:
    """
    Find quantity and sum of given list's numbers which are dividing by 5 but not dividing by 7.

    :param list_: Any list of integers
    :return: Tuple of sum and quantity which satisfy given condition

    :Example:

    In this example (205, 3) will be returned as (sum, quantity) of only numbers from
        list [5, 50, 3, 150, 11] which are dividing by 5 and not dividing by 7

    .. doctest::

        >>> print(sum_div5_notdiv7([5, 50, 3, 150, 11]))
        (205, 3)
    """
    sum_ = 0
    counter = 0
    for i, _ in enumerate(list_):
        if ((list_[i] % 5) == 0) and ((list_[i] % 7) != 0):
            sum_ += list_[i]
            counter += 1
    return sum_, counter


def print_solution():
    """"Validate input, generate list of given length, find quantity and sum, print results."""
    natural = 15
    list_of_int = []
    if is_natural(natural):
        for _ in range(int(natural)):
            list_of_int.append(random.randint(-1000, 1000))
        sum_, counter = sum_div5_notdiv7(list_of_int)
        print(list_of_int)
        print("Sum of all items, which satisfy the condition:  \t", sum_)
        print("Count of all items, which satisfy the condition:\t", counter)
    else:
        print("Invalid input. Please write correct natural number")


if __name__ == '__main__':
    print_solution()
