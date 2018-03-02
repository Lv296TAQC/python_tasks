"""This module solves the task 559 from zadachi.pdf"""

from math import sqrt

RANGE_PRIME_NUMBERS = 48


def prime_number():
    """
    Find all smaller numbers of Mersenne numbers

    Args:
        n_number(int): any natural number

    Return:
        list, which returns a simple mercenary number that
        is less than the entered number in the input field
    """
    generated_number = [2]
    for k in range(3, RANGE_PRIME_NUMBERS + 1, 2):
        if k > 10 and k % 10 == 5:
            continue
        for j in generated_number:
            if j > int((sqrt(k)) + 1):
                generated_number.append(k)
                break
            if k % j == 0:
                break
        else:
            generated_number.append(k)
    return generated_number


if __name__ == '__main__':
    LIST_OF_NUMBERS = []
    INPUT_N = input('Enter n: ')
    for i in prime_number():
        temp = 2 ** i - 1
        if temp < int(INPUT_N):
            LIST_OF_NUMBERS.append(temp)
        else:
            break
    print(LIST_OF_NUMBERS)
