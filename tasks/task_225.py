""""This module solves the task 225."""


def func3(number: int) -> list:
    """
    Take a natural number and return the list of numbers,
     where entered number is divisible by q**2 and not divisible by q**3.

    :param number: Any natural number.
    :return mylist: List of all numbers divisible by q**2 and not divisible by q**3.

    >>> func3(100)
    [2, 5, 10]
    """
    q_number = 1
    mylist = []
    while q_number <= number:
        if number % q_number**2 == 0 and number % q_number**3 != 0:
            mylist.append(q_number)
            q_number += 1
        else:
            q_number += 1
    return mylist
