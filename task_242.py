import math


def total_sum(n):
    sum = 0
    for k in range(n+1):
        print(k)
        x = ((-1) ** (k * (k - 1) * 0.5)) / math.factorial(k)
        sum += x
    return sum


print(total_sum(2))
