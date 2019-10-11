# Задание 1. Уровень - легкотня.
# Условие: сейчас каждый пользуется мессенжерами и соцсетями для того, чтобы сообщить информацию
# другому человеку. Но что было раньше? Раньше люди шли на почту и отправляли телеграммы.
# Телеграф передавал сообщение по символам - плата снималась за каждый символ.
# Допустим, что каждый символ (в том числе и пробел) стоит 23 коп. Сколько бы ты портатил за ежедневную переписку?


# Входные данные : строка - сообщение.
# Выходные данные : строка - стоимость отрпавки сообщения.


# Пример:
# Ввод:                                            # Вывод:

# Привет? Вацап? Кек :)                            4 р. 83 коп.

# BestPractice топ. Однозначно                     7 р. 59 коп.

# Ку-ка-ре-ку. PHP                                 3 р. 68 коп.


str = input()
print((len(str)*23//100), " p. ", (len(str)*23 % 100), " коп. ")