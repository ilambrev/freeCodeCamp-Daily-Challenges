from math import sqrt

def is_integer_hypotenuse(a, b):
    two_sides_sum = a ** 2 + b ** 2
    c = int(sqrt(two_sides_sum))

    return c ** 2 == two_sides_sum

# print(is_integer_hypotenuse(3, 4))
# print(is_integer_hypotenuse(2, 3))
# print(is_integer_hypotenuse(5, 12))
# print(is_integer_hypotenuse(10, 10))
# print(is_integer_hypotenuse(780, 1040))
# print(is_integer_hypotenuse(250, 333))