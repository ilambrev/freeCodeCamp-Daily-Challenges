from math import sqrt

def is_perfect_square(n):

    return False if n < 0 else sqrt(n).is_integer()


# print(is_perfect_square(9))
# print(is_perfect_square(49))
# print(is_perfect_square(1))
# print(is_perfect_square(2))
# print(is_perfect_square(99))
# print(is_perfect_square(-9))
# print(is_perfect_square(0))
# print(is_perfect_square(25281))