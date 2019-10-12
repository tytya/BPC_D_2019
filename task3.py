"""
Creator: Krylova Elizaveta
"""


R1 = int(input())
C1 = int(input())
R2 = int(input())
C2 = int(input())

if (abs(R1 - R2) == 2 and abs(C1 - C2) == 5) or (abs(R1 - R2) == 5 and abs(C1 - C2) == 2):
    print("YESSSS!")
else:
    print("No no")
