def fun1(n):
    res = []
    a , b = 0 , 1

    for i in range(n):
        res.append(a)
        a , b = b , a+b
    
    return res

def fun2(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        res = fun2(n-1)
        res.append(res[-1]+res[-2])
    
    return res

def fun3(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n ==2:
        return 1
    else:
        return fun3(n-1)+fun3(n-2)

x = fun1(12)
y = fun2(12)
z = fun3(12)

print(x, y, z)
