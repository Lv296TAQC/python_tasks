"""Finding interchangeable sum of digits n"""


def total_sum1(number):
    """Method finding total_sum"""
    array = [int(d) for d in str(number)]
    sum1 = 0
    for index, element in enumerate(array):
        if index % 2 == 0:
            sum1 += element
        else:
            sum1 -= element
    return sum1
