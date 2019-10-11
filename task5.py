"""
Creator: Krylova Elizaveta
"""


NUM = int(input())
DIVS = []
for i in range(1, NUM + 1):
    if NUM % i == 0:
        DIVS.append(i)

print(' '.join(map(str, DIVS)))

if len(DIVS) == 2:
    print("ACHTUNG")
