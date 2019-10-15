"""
Creator: Krylova Elizaveta
"""

LANGS = ""

while True:
    STR = input()
    if STR:
        LANGS += STR + "\n"
    else:
        break

LANGS = LANGS.split("\n")
del LANGS[-1]

LAN = []

for LANG in LANGS:
    LAN.append(LANG.split(" "))

TEXTES = ""

while True:
    STR = input().lower()
    if STR:
        TEXTES += STR + "\n"
    else:
        break

TEXTES = TEXTES.split("\n")
del TEXTES[-1]

TEX = []

for TEXT in TEXTES:
    TEX.append(TEXT.split(" "))

for TEXTS in TEX:
    OUTPUT = []
    for TEXT in TEXTS:
        DICT = {}
        for LANG in LAN:
            for TE in TEXT:
                if LANG[1].find(TE) != -1:
                    try:
                        DICT[LANG[0]] += 1
                    except KeyError:
                        DICT[LANG[0]] = 0
        MAX = -1
        k = 0
        for k, value in DICT.items():
            if value > MAX:
                MAX = value
                MAX_V = k
        try:
            OUTPUT.index(k)
        except ValueError:
            OUTPUT.append(k)
    OUTPUT.sort()
    print(*OUTPUT)
