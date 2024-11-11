input1 = """numpy1.21conda
scipy1.7conda
matplotlib3.4
pandas1.3conda
requests2.26pip"""

def fun(val):
    lns = val.strip().split()
    rs = []

    for ln in lns:
        if "conda" in ln:
            ln = ln.replace("conda","")
            for i in range(len(ln)):
                if ln[i].isdigit():
                    left = ln[:i]
                    rt = ln[i:]
                    rs.append(f"{left}={rt}")
                    break
    return rs

x = fun(input1)
print(x)

