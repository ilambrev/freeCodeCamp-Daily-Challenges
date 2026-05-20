def is_valid_isbn_13(s):
    def check_symbols_validity(s):
        for symbol in s:
            if not symbol.isdigit() and not symbol == "-":
                return False

        return True

    if not check_symbols_validity(s):
        return False

    digits = [int(symbol) for symbol in s if symbol.isdigit()]

    if not len(digits) == 13:
        return False

    digits_sum = sum([digits[i] if i % 2 == 0 else digits[i] * 3 for i in range(len(digits))])

    return check_symbols_validity(s) and digits_sum % 10 == 0

# print(is_valid_isbn_13("9780306406157"))
# print(is_valid_isbn_13("97803064061570"))
# print(is_valid_isbn_13("978-0-13-595705-9"))
# print(is_valid_isbn_13("978-030-64061A-4"))
# print(is_valid_isbn_13("9-7-8-0-1-3-4-7-5-7-5-9-9"))