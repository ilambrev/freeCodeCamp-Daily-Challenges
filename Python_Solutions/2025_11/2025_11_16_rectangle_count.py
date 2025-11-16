from math import factorial as f

def count_rectangles(width, height):
    c1 = f(width + 1) / (f(2) * f(width + 1 - 2))
    c2 = f(height + 1) / (f(2) * f(height + 1 - 2))

    return int(c1 * c2)

# print(count_rectangles(1, 3))
# print(count_rectangles(3, 2))
# print(count_rectangles(1, 2))
# print(count_rectangles(5, 4))
# print(count_rectangles(11, 19))