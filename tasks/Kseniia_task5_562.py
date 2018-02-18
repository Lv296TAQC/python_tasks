def partition(n):
    answer = []
    while n > 0:
        answer.append(n % 10)
        n /= 10
    return answer[::-1]


def func(a, b):
    answer = []
    for i in range(a, b):
        arr = partition(i)
        exp = len(arr)
        arr = [pow(x, exp) for x in arr]
        if sum(arr) == i:
            answer.append(i)
    return answer


print(func(10, 999))