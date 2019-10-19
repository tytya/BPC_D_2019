"""
Creator: Krylova Elizaveta
"""

N = int(input())

YRA = False
SOB = False

for j in range(N):
    STR = input().replace(' ', '').lower()
    STR = [i  for i in STR if i.isalpha() is True]
    for i in range(int(len(STR)/2)):
        if STR[i] != STR[-i-1]:
            if j % 2 == 0:
                YRA = True
            else:
                SOB = True
            break

if YRA is True:
    print("Сослан на Плутон Юра")
elif SOB is True:
    print("Сослан на Плутон собеседник")
else:
    print("Сослать обоих")
