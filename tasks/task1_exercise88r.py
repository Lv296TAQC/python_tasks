""""Write one to the start and to the end of given natural number"""

import sys


def one_bounds(natural):
    """Add one to the first and to the last digit, two to one-digit natural number

        Args:
            natural (int): Natural validated number from input

        Returns:
            int: Natural number with added one to the first and to the last digit

    """
    natural_most = natural
    counter = 1
    while natural_most > 9:
        natural_most = natural_most // 10
        counter *= 10
    if counter == 1:
        return natural + 2
    return natural + counter + 1


def input_and_validate():
    """Ask for input until valid data entered

            Returns:
                int: Natural number, but only if input data is valid

    """
    while True:
        natural = input("Enter natural (positive integer) number: ")
        if natural == 'bye' or natural == 'exit':
            sys.exit(0)
        try:
            natural = int(natural)
        except ValueError:
            print("Not a number, please write correct (natural number) value")
        else:
            if natural < 1:
                print("You entered not natural number, please enter positive integer number")
                continue
            return natural


def main():
    """"Ask for valid input, add numbers, print result"""
    natural = input_and_validate()
    num = one_bounds(natural)
    print(num)


if __name__ == '__main__':
    main()
