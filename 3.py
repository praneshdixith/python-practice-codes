input1 = """numpy 1.21conda
scipy 1.7conda
matplotlib 3.4
pandas 1.3conda
requests 2.26pip"""

def fun(val):
    iput = val.strip().split('\n')
    #lns = val.strip().split()
    out = []
    for i in iput:
        if "conda" in i or "pip" in i:
            a = i.replace("conda", "").replace("pip", "")
            for j in range(len(i)):
                if a[j].isdigit():  #if ln[i].isdigit():
                    pre = a[:j]
                    post = a[j:]
                    out.append(f"{pre} = {post}")
                    break
    return out

x = fun(input1)
print(x)