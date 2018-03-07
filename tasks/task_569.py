"""Added methods for veryfying prime number and the division on prime numbers. Solves task 561 from zadachi.pdf"""


def is_prime(number_to_check: int) -> bool:
    """
    Method checks if number is prime.

    :param: Natural validated number from Input
    :return: boolean value True/False
    :Example:

    In this example is_prime(10) will return False because 10 is not a prime number
                    is_prime(5) will return True because 5 is a prime number

    ..doctest::

       >>>print(is_prime(10))
       False
       >>>print(is_prime(5))
       True
    """

    for num in range(2, number_to_check):
        if (number_to_check % num) == 0:
            return False
    return True


def prime_numbers(number: int) -> int:
    """
    Method checks the array of prime numbers from the range

    :param: Natural validated number from Input
    :return: array of natural numbers

    :Example:

    In this example we'll have array of prime numbers

    ..doctest::

       >>>print(prime_numbers(9)
       [7]
       >>>print(prime_numbers(18))
       [7, 11, 13, 17]
    """

    array = []
    for num in range(6, number):
        if is_prime(num):
            array.append(num)
    return array


def divide_by_prime(number: int) -> bool:
    """
    Method checks division on prime numbers

    :param: Natural validated number from Input
    :return: boolean value True/False

    :Example:

    In this example we'll have boolean values

    ..doctest::

      >>>print(divide_by_prime(14))
      True
      >>>print(divide_by_prime(5))
    """
    for num in prime_numbers(number):
        if (number % num) == 0:
            return True
    return False


def validate(number: int) -> bool:
    """
    Methods checks division on prime numbers 2, 3, 5 and not division on other prime numbers

    :param: Natural validated number from Input
    :return: boolean value True/False

    :Example:

    In this example we'll have boolean values

    ..doctest::

      >>>print(validate(30))
      True
      >>>print(validate(7))
      False
    """
    return number % 2 == 0 and number % 3 == 0 and number % 5 == 0 and not divide_by_prime(number)


def natural_numbers(number: int) -> int:
    """
    Method is the solution of the task_569

    :param: Natural validated number from Input
    :return: array

    :Example:

    In this example we'll have array

    ..doctest::

      >>>print(natural_numbers(5))
      [20, 60, 90, 120, 150]
    """
    result = []
    current_count = 0
    current = 1
    while current_count < number:
        if validate(current):
            result.append(current)
            current_count += 1
        current += 1
    return result
