"""
This module solves task 561 from zadachi.pdf.
"""

from math import sqrt
from sys import argv


def squares_of_numbers(value):
    """
    Description: find numbers that correspond
                 to the last records of their square.
    Arg: int number.
    Result: list of numbers.
    """
    for number in range(1, int(value)):
        if sqrt(number).is_integer():
            if str(int(sqrt(number))) == str(number)[-(len(str(number)) - 1):]:
                print(f"{int(sqrt(number))}^2 = {number}")


try:
    squares_of_numbers(argv[1])
except ValueError:
    print("Inputted data isn't integer.")
