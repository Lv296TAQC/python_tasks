def func(n):
    answer = []
    for i in range(n):
        for j in range(n):
            if i * i + j * j == n and i >= j:
                answer.append((i, j))
    return answer


print(func(100))