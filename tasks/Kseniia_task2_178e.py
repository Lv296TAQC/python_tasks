from math import factorial


def func(arr):
    count = 0
    for index, elem in enumerate(arr):
        if elem > pow(2, index) and elem < factorial(index):
            count += 1


    return count


print(func([0, 0, 1, 6, 23, 33]))