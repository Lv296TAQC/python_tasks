"""
This module solves task 243_a from zadachi.pdf.
"""

from sys import argv


def sum_of_two_squares(number):
    """
    Description: converts string into int,
                 checks whether the number is the sum
                 of the squares of two numbers.

    Arg: string in int number format, like "21".

    Return: tuple with squares of two numbers.

    """
    number = int(number)
    first = 1
    while first ** 2 <= number:
        second = 1
        while second ** 2 <= number:
            if first**2 + second**2 == number:
                return first, second
            second += 1
        first += 1
    return False


def main():
    """Start 'sum_of_two_squares' function."""
    try:
        if sum_of_two_squares(argv[1]):
            first_square, second_square = sum_of_two_squares(argv[1])
            print(f"The number {argv[1]} is the sum", end=" ")
            print("of the squares of two numbers:")
            print(f"{argv[1]} = {first_square}^2 + {second_square}^2")
        else:
            print(f"The number {argv[1]} isn't the sum", end=" ")
            print("of the squares of two numbers.")
    except ValueError:
        print("Please type number in string format, like '27'.")


if __name__ == "__main__":
    main()
