def fun(n):

    rel = []
    a , b = 0 , 1
    for i in range(n):
        rel.append(a)
        a , b = b , a+b

    return rel

x = fun(12)
print(x)
