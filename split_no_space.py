input1 = """numpy1.21conda
scipy1.7conda
matplotlib3.4
pandas1.3conda
requests2.26pip""" 

def funspl(val):
    ln = val.strip().split('\n')
    result = []

    for line in ln:
        if "conda" in line:
           line = line.replace("conda", "")
           for i in range(len(line)):
                if line[i].isdigit():
                    left = line[:i]
                    rt = line[i:]
                    result.append(f"{left}={rt}")
                    break

    return result

x = funspl(input1)
print(x)

