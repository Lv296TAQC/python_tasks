""""This module solves the task 325."""


def func4(number):
    """"
    Take natural number and return all simple divisors of entered number.

    Args:
        number (int): any natural number

    Returns:
        mylist (list): list of all simple divisors of entered number

    """
    i = 2
    mylist = []
    while i * i <= number:
        while number % i == 0:
            mylist.append(i)
            number = int(number / i)
        i += 1
    if number > 1:
        mylist.append(number)
    return mylist
