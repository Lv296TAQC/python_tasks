"""This module solves the task 329 from zadachi.pdf"""


def sum_of_digits(number):
    """"
    Return the sum of digits of entered number

    Arg:
        number(int): any natural number

    Return:
        int, where return sum of the digits
    """
    translate_var = str(number)
    result_integer = 0
    for i in translate_var:
        result_integer += int(i)
    return result_integer


def main_func(n_number, m_number):
    """
    Get all smaller and natural numbers, the square of the sum of the digits of which is equal to m.

    Arg:
        n_number(int): any natural number
        m_number(int): any natural number

    Return:
        list, where the numbers returned, the sum of digits equal to m.
    """
    counter_list = []
    for i in range(n_number):
        if pow(sum_of_digits(i), 2) == m_number:
            counter_list.append(i)
    return counter_list


if __name__ == '__main__':
    print(main_func(24, 36))
