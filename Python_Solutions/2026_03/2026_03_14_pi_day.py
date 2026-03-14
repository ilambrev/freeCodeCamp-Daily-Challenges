from decimal import Decimal, getcontext

def get_pi_decimal(n):
    getcontext().prec = n + 10
    C = 426880 * (10005 ** 0.5)
    
    num_iterations = n // 14 + 1
    
    P = Decimal(1)
    Q = Decimal(1)
    T = Decimal(13591409)
    
    L = 13591409
    X = 1
    M = 1
    K = 6
    S = Decimal(L)
    
    for i in range(1, num_iterations):
        M = (K**3 - 16*K) * M // i**3
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
        
    pi = Decimal(426880) * Decimal(10005).sqrt() / S

    pi_string = format(pi, 'f')

    return int(pi_string[n + 1])

# print(get_pi_decimal(5))
# print(get_pi_decimal(10))
# print(get_pi_decimal(22))
# print(get_pi_decimal(39))
# print(get_pi_decimal(76))
# print(get_pi_decimal(384))
# print(get_pi_decimal(601))
# print(get_pi_decimal(1000))