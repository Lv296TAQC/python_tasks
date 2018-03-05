"""This module solves the task 226 from zadachi.pdf"""


def common_multiple(n_number, m_number):
    """
    Get all their natural common multiples, smaller mn

    Arg:
        n_number(int): any natural number
        m_number(int): any natural number

    Return:
        list, which returns common multiples, smaller mn
    """

    counter = []
    for i in range(1, m_number * n_number):
        if i % m_number == 0 and i % n_number == 0:
            counter.append(i)
    return counter


if __name__ == '__main__':
    print("Common multiple: " + str(common_multiple(12, 22)))
