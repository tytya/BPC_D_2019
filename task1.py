"""
Creator: Krylova Elizaveta
"""

class Rational:
    """This class"""
    def __init__(self, num=0, den=1):
        self.num = num
        self.den = den
        if (self.den < 0 or self.num < 0):
            self.frac = "-" + str(self.num) + " / " + str(self.den)

        elif self.den == 0:
            print("ОШИБКА! Делитель равен 0")
            self.frac = str(self.num) + " / " + str(self.den)

        else:
            self.frac = str(self.num) + " / " + str(self.den)

    @classmethod
    def lcm(cls, first, second):
        """This method"""
        if first > second:
            greater = first
        else:
            greater = second
        while True:
            if((greater % first == 0) and (greater % second == 0)):
                l_c_m = greater
                break
            greater += 1
        return l_c_m

    @classmethod
    def gcd(cls, first, second):
        """This method"""
        while second:
            first, second = second, first % second
        return first

    @classmethod
    def separation(cls, s_t_r):
        """This method"""
        s_t_r = s_t_r.get()
        s_tr = s_t_r.split(" ")
        num = s_tr[0]
        den = s_tr[2]
        return num, den

    def add(self, f_r_a_c):
        """This method"""
        num1, den1 = self.separation(f_r_a_c)
        num1 = int(num1)
        den1 = int(den1)
        l_c_m = self.lcm(self.den, den1)
        num1 = num1 * (l_c_m/ den1)
        self.num = self.num * (l_c_m / self.den)
        num1 = num1 * (l_c_m/den1)
        s_u_m = self.num + num1
        g_c_d = self.gcd(s_u_m, l_c_m)
        return str(int(s_u_m / g_c_d)) + " / " + str(int(l_c_m / g_c_d))

    def sub(self, f_r_a_c):
        """This method"""
        num1, den1 = self.separation(f_r_a_c)
        num1 = int(num1)
        den1 = int(den1)
        l_c_m = self.lcm(self.den, den1)
        num1 = num1 * (l_c_m/ den1)
        self.num = self.num * (l_c_m / self.den)
        num1 = num1 * (l_c_m/den1)
        s_u_m = self.num - num1
        g_c_d = self.gcd(s_u_m, l_c_m)
        return str(int(s_u_m / g_c_d)) + " / " + str(int(l_c_m / g_c_d))

    def mult(self, f_r_a_c):
        """This method"""
        num1, den1 = self.separation(f_r_a_c)
        num1 = int(num1)
        den1 = int(den1)
        m_u_l_t_n = self.num * num1
        m_u_l_t_d = self.den * den1
        g_c_d = self.gcd(m_u_l_t_n, m_u_l_t_d)
        return str(int(m_u_l_t_n / g_c_d)) + " / " + str(int(m_u_l_t_d / g_c_d))

    def div(self, f_r_a_c):
        """This method"""
        num1, den1 = self.separation(f_r_a_c)
        num1 = int(num1)
        den1 = int(den1)
        m_u_l_t_n = self.num * den1
        m_u_l_t_d = self.den * num1
        g_c_d = self.gcd(m_u_l_t_n, m_u_l_t_d)
        return str(int(m_u_l_t_n / g_c_d)) + " / " + str(int(m_u_l_t_d / g_c_d))

    def get(self):
        """This method"""
        return self.frac
