"""This module solves the task 178b from zadachi.pdf"""


def multiple_numbers(list_of_n_numbers):
    """
    Determine the number of numbers that are multiples of 3 and not multiple 5

    Arg:
        list_of_n_numbers(list): list of natural number

    Return:
        int, which return count of list_of_n_numbers
    """

    counter = 0
    for i in list_of_n_numbers:
        if i % 3 == 0 and i % 5 == 1:
            counter += 1
    return counter


if __name__ == '__main__':
    print(multiple_numbers(list_of_n_numbers=[6, 21, 36, 51, 66, 81, 96, 111, 126]))
