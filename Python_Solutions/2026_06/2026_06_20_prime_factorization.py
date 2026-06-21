def prime_factorization(n):
    multiplayer = 2
    multiplayers = []
    current_result = 1

    while current_result < n:
        step = current_result * multiplayer 
        if n % step == 0:
            multiplayers.append(multiplayer)
            current_result = step
        else:
            multiplayer += 1

    return multiplayers

# print(prime_factorization(20))
# print(prime_factorization(17))
# print(prime_factorization(15))
# print(prime_factorization(35))
# print(prime_factorization(999))
# print(prime_factorization(360))
# print(prime_factorization(510510))