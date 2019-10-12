"""
Creator: Krylova Elizaveta
"""


ROW1 = int(input())
COL1 = int(input())
ROW2 = int(input())
COL2 = int(input())

if abs(ROW1 - ROW2) == 2 or abs(ROW1 - ROW2) == 5:
    if abs(COL1 - COL2) == 2 or abs(COL1 - COL2) == 5:
        print("YESSSS!")
else:
    print("No no")
