def is_valid_isbn10(s):
    s = s.replace("-", "")
    last_symbol = s[-1]

    digits = [int(d) for d in s[:-1] if d.isdigit()]

    if not len(digits) == 9:
        return False

    if not (last_symbol.isdigit() or last_symbol == "X"):
        return False

    if last_symbol.isdigit():
        digits.append(int(last_symbol))
    else:
        digits.append(10)

    digits_sum = sum([digits[i-1] * i for i in range(1, len(digits) + 1)])

    return digits_sum % 11 == 0

# print(is_valid_isbn10("0-306-40615-2"))
# print(is_valid_isbn10("0-306-40615-1"))
# print(is_valid_isbn10("0-8044-2957-X"))
# print(is_valid_isbn10("X-306-40615-2"))
# print(is_valid_isbn10("0-6822-2589-4"))