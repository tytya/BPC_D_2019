"""
Creator: Krylova Elizaveta
"""


P1, P2 = [], []
CHECK = False

for i in range(8):
    El1, El2 = map(int, input().split())
    P1.append(El1)
    P2.append(El2)


for i in range(8):
    for j in range(i + 1):
        if P1[i] != (8 or 1) and P2[i] != (8 or 1) and P1[j] != (8 or 1) and P2[j] != (8 or 1):
            if P1[i] - P1[j] == P2[i] - P2[j]:
                CHECK = True
                break

if CHECK is False:
    print("NO")
else:
    print("YES")
    