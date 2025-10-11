def hex_to_decimal(hex):
    map = {"0": 0,
           "1": 1,
           "2": 2,
           "3": 3,
           "4": 4,
           "5": 5,
           "6": 6,
           "7": 7,
           "8": 8,
           "9": 9,
           "A": 10,
           "B": 11,
           "C": 12,
           "D": 13,
           "E": 14,
           "F": 15}

    reversed_hex_num = hex[::-1]

    return sum([map[reversed_hex_num[n]] * 16 ** n for n in range(0, len(reversed_hex_num))])

# print(hex_to_decimal("A"))
# print(hex_to_decimal("15"))
# print(hex_to_decimal("2E"))
# print(hex_to_decimal("FF"))
# print(hex_to_decimal("A3F"))