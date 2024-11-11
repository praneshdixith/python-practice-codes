
def fibnu(rang):
    seq = []
    a , b  = 0 , 1
    for _ in range(rang):
        seq.append(a)
        a , b = b , a+b 

    return seq[-1], seq

x , y = fibnu (12)
print(x, y )
