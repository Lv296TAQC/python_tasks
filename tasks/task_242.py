"""Calculate the expression"""
import math
def total_sum(number_n):
    """Method for calculating the total sum in the range"""
    sum1 = 0
    for k in range(number_n+1):
        print k
        formula = ((-1) ** (k * (k - 1) * 0.5)) / math.factorial(k)
        sum1 += formula
    return sum1




