"""
This module solves task 561 from zadachi.pdf.
"""

from sys import argv


def squares_of_numbers(value):
    """
    Description: find numbers that correspond
                 to the last records of their square.

    Arg: int number.

    Result: list of int numbers.

    """
    result = []
    for number in range(1, value):
        squares = str(number ** 2)
        number = str(number)
        if squares.endswith(number):
            result.append(f"{number}^2 = {squares}")
    return result


def main():
    """Start 'squares_of_numbers' function."""
    try:
        squares = squares_of_numbers(int(argv[1]))
        for element in squares:
            print(element)
    except ValueError:
        print("Inputted data isn't integer.")


if __name__ == "__main__":
    main()
