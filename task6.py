# Задание 6. Уровень - Кодзима, ты ли это?
# Условие: вы создали игру в жанре шутер. Теперь ваш дизайнер придумал новое неизвестное никому оружее - дробовик.
# Известно, что дробовики стреляют дробью (внезапно, правда?). Ваша задача - рассчитать суммарный урон, наненсенный
# выстрелом из дробовика.


# Входные данные : Сначала вводится количество дробинок.
# Затем урон от каждой дробинки. Урон от каждой дробинки выражается простой дробью,
# её числитель и знаменатель вводятся на отдельных строках.

# Выходные данные : Суммарный урон, выраженный простой несократимой дробью с дробной
# чертой между числителем и знаменателем.


# Пример:
# Ввод:                                               # Вывод:
# 2
# 1
# 50
# 3
# 20                                                 17/100


# 3
# 1
# 50
# 2
# 40
# 3
# 30                                                 17/100

def LCM(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a



n = int(input())
num = int(input())
lcm = int(input())

for i in range(n-1):
    w = int(input())
    f = int(input())
    f_1 = lcm
    lcm = LCM(lcm, f)
    w = w*(lcm/f)
    num = num*(lcm/f_1) + w

gcd = GCD(num, lcm)

print(round(num/gcd), "/", round(lcm/gcd))