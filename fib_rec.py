def fibrec(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        res = fibrec( n - 1)
        res.append(res[-1]+res[-2])

        return res

x = fibrec(12)
print(x)


def func(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return func(n-1)+func(n-2)

y = func(12)
print(y)

