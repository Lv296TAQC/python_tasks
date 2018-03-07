"""This module solves the task 559 from zadachi.pdf"""


def is_prime_number(check_number):
    """
    Сheck whether the number is simple

    Args:
        check_number(int):any natural number

    Return:
        boolean value
    """
    for i in range(2, check_number):
        if (check_number % i) == 0:
            return False
    return True


def return_prime_number(limit_number):
    """
    Output a simple number found by the function is_prime_number

    Args:
        limit_number(int): any natural number

    Return:
        list, which returns prime numbers
    """
    list_of_number = []
    for counter_number in range(2, limit_number):
        if is_prime_number(counter_number):
            list_of_number.append(counter_number)
    return list_of_number


def number_of_mercenn(limit_number):
    """
    Find all smaller numbers of Mersenne.

    Args:
        limit_number(int): any natural number

    Return:
        list, which return prime number of Mercenns
    """
    list_of_mercenne_number = []
    for p_number in return_prime_number(limit_number):
        formula_of_number_marcenne = 2 ** p_number - 1
        if formula_of_number_marcenne < limit_number:
            list_of_mercenne_number.append(formula_of_number_marcenne)
        else:
            break
    return list_of_mercenne_number
