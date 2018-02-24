def update(p, q, a):
    if (p <= q) or (q < 0):
        return 'incorrect values'
    for k, element in enumerate(a):
        if abs(element) % p == q:
            a[k] = 0
    return a

#example print(update(2, 1, [3 , 4]))