def lcm(a, b):
    max_value = max(a, b)
    min_value = min(a, b)
    x = max_value % min_value

    while x > 0:
        max_value = min_value
        min_value = x
        x = max_value % min_value

    return int((a * b) / min_value)

# print(lcm(4, 6))
# print(lcm(9, 6))
# print(lcm(10, 100))
# print(lcm(13, 17))
# print(lcm(45, 70))