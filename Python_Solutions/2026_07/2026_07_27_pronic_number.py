def is_pronic(n):
    i = 0
    product = i ** 2 + i

    while product < n:
        i += 1
        product = i ** 2 + i

    return product == n

# print(is_pronic(6))
# print(is_pronic(15))
# print(is_pronic(12))
# print(is_pronic(132))
# print(is_pronic(80))
# print(is_pronic(0))