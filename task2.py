"""
Creator: Krylova Elizaveta
"""

N = int(input())
PLANET = input()
PLANET = PLANET.split(" ")
DICT = {}

for i in range(N):
    DICT[PLANET[i]] = N - i

L_NUM = list(DICT.values())
L_QUA = list(DICT.keys())


MAX = -1

for i in range(len(DICT)):
    if L_NUM[i] > MAX:
        MAX = L_NUM[i]
        MAX_N = i

print(L_QUA[MAX_N])
