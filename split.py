val1 = """numpy 1.21 conda
scipy 1.7 conda
matplotlib 3.4
pandas 1.3 conda
requests 2.26 pip"""

def filter(val):
    rel = []
    ln = val.strip().split('\n')

    for line in ln:
        spt = line.split()
        if len(spt)>=3 and spt[2] == "conda":
            print(f"{spt[0]} = {spt[1]}")
            rel.append(f"{spt[0]} = {spt[1]}")

    return rel

rel = filter(val1)
print(rel)

