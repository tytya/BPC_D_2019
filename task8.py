# Задание 8. Уровень - жестоко.

# Условие: напишите программу, которая для данного текста подсчитывает частоты всех символов в нем.
# Регистр не важен. То есть символы 'А' и 'а' - эквивалентны.



# Входные данные: произвольный текст.

# Выходные данные: таблица с частотами символов.
# Таблица должна быть отсортирована по убыванию частот, в случае равных частот — в алфавитном порядке.
# Если в тексте нет алфавитных символов - выводим перенос строки.

# Пример:
# Ввод:                                      # Вывод:
# hello, world!                              l: 3
#                                            o: 2
#                                            d: 1
#                                            e: 1
#                                            h: 1
#                                            r: 1
#                                            w: 1



str = input().lower()
str = list(str)
str.sort()
dict = {}
for s in str:
    if s.isalpha():
        try:
            dict[s] +=1
        except:
            dict[s] = 1


list_d = list(dict.items())

list_d.sort(reverse=True, key=lambda i: i[1])

dict = {}

for i in list_d:
    dict[i[0]] = i[1]
    print(i[0], ':', i[1])

print(dict)
