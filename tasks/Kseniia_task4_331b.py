def func(n):
    answer = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i * i + j * j + k * k == n and i >= j and j >= k:
                    answer.append((i, j, k))
    return answer


print(func(100))