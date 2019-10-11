"""
Creator: Krylova Elizaveta
"""

STR = input().lower()
STR = list(STR)
STR.sort()
DICT = {}
for s in STR:
    if s.isalpha():
        try:
            DICT[s] += 1
        except KeyError:
            DICT[s] = 1


LIST_D = list(DICT.items())

LIST_D.sort(reverse=True, key=lambda i: i[1])

if LIST_D != []:

    DICT = {}

    for i in LIST_D:
        DICT[i[0]] = i[1]
        print(i[0], ':', i[1])

    print(DICT)
else:
    print("\n")
