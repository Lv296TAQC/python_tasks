"""
This module solves task 88_б from zadachi.pdf.
"""

from sys import argv


def reverse_int(number):
    """
    Description: convert int number to string,
                 reverse it and return as int number.
    Arg: int number.
    Return: reversed int number.
    """
    return int(number[::-1])


try:
    print(reverse_int(argv[1]))
except ValueError:
    print("Inputted data isn't integer.")
