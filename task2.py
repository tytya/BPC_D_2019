"""
Creator: Krylova Elizaveta
"""

NUMB1 = float(input())
NUMB2 = float(input())
STR = input()

if STR == "+":
    print(round((NUMB1 + NUMB2), 1))
elif STR == "-":
    print(round((NUMB1 - NUMB2), 1))
elif STR == "*":
    print(round((NUMB1 * NUMB2), 1))
elif STR == "/":
    if NUMB2 == 0:
        print("ЫЫЫЫЫЫ")
    else:
        print(round((NUMB1 / NUMB2), 1))
else:
    print("ЫЫЫЫЫЫ")
