"""
Creator: Krylova Elizaveta
"""



def lcm(first, second):
    """This function"""
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



def gcd(first, second):
    """This function"""
    while second:
        first, second = second, first % second
    return first


N = int(input())
NUM = int(input())
LCM = int(input())

for i in range(N-1):
    W = int(input())
    F = int(input())
    F1 = LCM
    LCM = lcm(LCM, F)
    W = W*(LCM/F)
    NUM = NUM*(LCM/F1) + W

GCD = gcd(NUM, LCM)

print(round(NUM/GCD), "/", round(LCM/GCD))
