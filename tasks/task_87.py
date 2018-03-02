"""This module solves the task 87 from zadachi.pdf"""


def natural_number(n_number, m_number):
    """
    Get the sum of the last digits of the number n.

    Arg:
       n_number(int): any natural number
       m_number(int): any natural number

    Return:
        int, where the last digits are sum
    """
    counter = 0
    while m_number > 0:
        counter += n_number % 10
        n_number //= 10
        m_number -= 1
    return counter


if __name__ == "__main__":
    print('Last digits of the number n: ', natural_number(2322, 2))
