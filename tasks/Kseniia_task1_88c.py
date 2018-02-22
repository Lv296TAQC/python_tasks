from math import log10


def func(n):
    rank = pow(10, int(log10(n)))
    first = n // rank
    last = n % 10
    return n - (first - last) * rank - last + first


print(func(1356))