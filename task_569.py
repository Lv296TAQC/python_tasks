"""Added methods for veryfying prime number and the division on prime numbers"""
def is_prime(number_to_check):
    """Check if number is prime."""
    for num in range(2, number_to_check):
        if (number_to_check % num) == 0:
            return False
    return True

def prime_numbers(number):
    """Check the list of prime numbers from the range."""
    array = []
    for num in range(6, number):
        if is_prime(num):
            array.append(num)
    return array

def divide_by_prime(number):
    """Check division on prime numbers."""
    for num in prime_numbers(number):
        if (number % num) == 0:
            return True
    return False

def validate(number):
    """Check division on prime numbers."""
    return number % 2 == 0 and number % 3 == 0 and number % 5 == 0 and not divide_by_prime(number)

