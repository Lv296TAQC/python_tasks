""""This module solves the task 225."""


def func3(number):
    """"
    Take a natural number and return the list of numbers,
     where entered number is divisible by q**2 and not divisible by q**3.

    Args:
        number (int): any natural number

    Returns:
        mylist (list): list of all numbers divisible by q**2 and not divisible by q**3

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
