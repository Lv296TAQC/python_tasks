"""Added methods for veryfying prime number and the division on prime numbers. Solves task 561 from zadachi.pdf"""


def is_prime(number_to_check):
    """
    Method checks if number is prime

    Arg:
        natural numbers
    Return:
        True/False
    Example:
        print(is_prime(10))--> False
        print(is_prime(5))--> True
    """

    for num in range(2, number_to_check):
        if (number_to_check % num) == 0:
            return False
    return True

def prime_numbers(number):
    """
    Method checks the array of prime numbers from the range

    Arg:
        natural numbers
    Return:
        array of prime numbers
    Example:
        print(prime_numbers(9)) --> [7]
        print(prime_numbers(18)) --> [7, 11, 13, 17]
    """

    array = []
    for num in range(6, number):
        if is_prime(num):
            array.append(num)
    return array

def divide_by_prime(number):
    """
    Method checks division on prime numbers.

    Arg:
        natural numbers
    Return:
        True/False
    Example:
        print(divide_by_prime(14)) --> True
        print(divide_by_prime(14))--> False
    """
    for num in prime_numbers(number):
        if (number % num) == 0:
            return True
    return False

def validate(number):
    """
    Methods checks division on prime numbers 2, 3, 5 and not devision on other prime numbers

    Arg:
        natural numbers
    Return:
        True/False
    Example:
         print(validate(30)) --> True
         print(validate(7)) --> False
    """
    return number % 2 == 0 and number % 3 == 0 and number % 5 == 0 and not divide_by_prime(number)

def natural_numbers(number):
    """
    Method is the solution of the task_569

    Arg:
        natural numbers
    Return:
        array of the numbers
    Example:
        print(natural_numbers(5)) --> [20, 60, 90, 120, 150]
    """
    result = []
    current_count = 0
    current = 1
    while current_count < number:
        if validate(current):
            result.append(current)
            current_count+=1
        current+=1
    return result
