"""
Creator: Krylova Elizaveta
"""

N = int(input())
for i in range(N):
    ST = list(input())

    j = 0
    CH = True
    while CH:
        CH = False
        while j < len(ST)-1:
            if (ST[j] + ST[j+1]) == "()" or (ST[j] + ST[j+1]) == "[]" or (ST[j] + ST[j+1]) == "{}":
                ST.pop(j)
                ST.pop(j)
                CH = True
            else:
                j = j + 1
        j = 0
    LEN = len(ST)
    if LEN == 0:
        print('yes')
    else:
        print('no')
