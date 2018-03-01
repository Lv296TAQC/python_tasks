"""
This module solves task 178_г from zadachi.pdf.
"""

from sys import argv


def task_function(numbers):
    """
    Description: checks how namy numbers in list are less than
                 the sum of the previous and next numbers.
    Args: list of int numbers.
    Return: count of numbers that are less than
            the sum of the previous and next numbers.
    """
    numbers = list(map(int, numbers))
    count = 0
    for first, second, third in zip(numbers, numbers[1:], numbers[2:]):
        if (first + third) / 2 > second:
            count += 1
    return count


try:
    print("Elements that correspond to the task condition:",
          task_function(argv[1:]))
except ValueError:
    print("Inputted data isn't integer.")
