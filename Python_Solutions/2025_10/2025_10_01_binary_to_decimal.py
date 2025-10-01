def to_decimal(binary):
    decimal_number = 0

    for i in range(len(binary)):
        decimal_number += int(binary[len(binary) - 1 - i]) * 2 ** i

    return decimal_number

# print(to_decimal("101"))
# print(to_decimal("1010"))
# print(to_decimal("10010"))
# print(to_decimal("1010101"))