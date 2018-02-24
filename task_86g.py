def total_sum(number):
    array = [int(d) for d in str(number)]
    sum = 0
    for index, element in enumerate(array):
        if index % 2 == 0:
            sum+=element
        else:
            sum-=element

    return sum

print(total_sum(5))
