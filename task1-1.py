# Задача 1. Уровень - математик.
# Условие: Вам необходимо создать калькулятор обыкновенных дробей.
# Создайте класс Rational , который обладает следующими свойствами:
# 1) конструктор класса по умолчанию создает дробь вида 0 / 1
# 2) если у конструктора класса указано оба аргумента A и B (целые числа), то создается дробь вида A/B
# 3) если созданная дробь отрицательна - то минус ставится у числителя (-A/B)
# 4) если B = 0 - сообщение об ошибке и проинициализируйте дробь значением по умолчанию (0 / 1)
# 5)Создайте методы add(), sub(), div(), mult() для сложения, вычитания, умножения и деления дробей, резульатами всех
# этих операций должны быть НЕСОКРАТИМЫЕ ДРОБИ
# реализовать их можно в свободной форме. Пример реализации:
# a = Rational(1,2)
# b = Rational()
# c = a.add(b)
# d = a.sub(b)
# 6) создайте метод get() для вывода дроби в выходной поток . Выводить дробь надо в виде строки "A / B"


class Rational:
    def __init__(self, A = 0, B = 1):
        self.A = A
        self.B = B
        if (self.B < 0 or self.A < 0):
            self.FRAC = "-" + self.A + " / " + self.B
        elif (self.B == 0):
            print("ОШИБКА! Делитель равен 0")
            self.FRAC = self.A + " / " + self.B 
        else:
            self.FRAC = str(self.A) + " / " + str(self.B)

    def lcm(self, first, second):
     
        if first > second:
            greater = first
        else:
            greater = second
        while True:
            if((greater % first == 0) and (greater % second == 0)):
                print("0")
                l_c_m = greater
                break
            print("0")
            greater += 1
        return l_c_m

    def gcd(self, first, second):
        """This function"""
        while second:
            first, second = second, first % second
        return first

    def separation(self, STR):
        STR = STR.get()
        S = STR.split(" ")
        A = S[0]
        B = S[2]
        return A, B

    def add(self, F):
        A1, B1 = self.separation(F)
        A1 = int(A1)
        B1 = int(B1)
        print("0")
        GCD = self.gcd(self.B, B1)
        print("0")
        A1 = A1 * (GCD / B1)
        self.A = self.A * (GCD / self.B)
        SUM = self.A + A1
        print("0")
        LCM = self.lcm(SUM, GCD)
        print("0")
        return ((SUM / LCM) + " / " + (GCD / LCM))

    def sub(self):
        pass
    def mult(self):
        pass
    def div(self):
        pass
    def get(self):
        return self.FRAC 


a = Rational(2, 5)
b = Rational(4, 25)

print (a.add(b))