"""Finding interchangeable sum of digits n. Solves task 86d from zadachi.pdf"""


def total_sum1(number):
    """
    Method finds interchangeable sum of n number

    Arg:
        natural numbers
    Return:
        interchangeable sum digits of n number
    Example:
        print(total_sum1(3)) --> 3
        print(total_sum(10))-->  1
    """
    array = [int(d) for d in str(number)]
    sum1 = 0
    for index, element in enumerate(array):
        if index % 2 == 0:
            sum1 += element
        else:
            sum1 -= element
    return sum1
