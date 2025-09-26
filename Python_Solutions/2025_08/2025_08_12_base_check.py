from string import digits, ascii_lowercase

def is_valid_number(n, base):
    symbols = (digits + ascii_lowercase)[:base]

    for symbol in n:
        if symbol.lower() not in symbols:
            return False
    
    return True

# print(is_valid_number("10101", 2))
# print(is_valid_number("10201", 2))
# print(is_valid_number("76543210", 8))
# print(is_valid_number("9876543210", 8))
# print(is_valid_number("9876543210", 10))
# print(is_valid_number("ABC", 10))
# print(is_valid_number("ABC", 16))
# print(is_valid_number("Z", 36))
# print(is_valid_number("ABC", 20))
# print(is_valid_number("4B4BA9", 16))
# print(is_valid_number("5G3F8F", 16))
# print(is_valid_number("5G3F8F", 17))
# print(is_valid_number("abc", 10))
# print(is_valid_number("abc", 16))
# print(is_valid_number("AbC", 16))
# print(is_valid_number("z", 36))