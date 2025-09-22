def digits_or_letters(s):
    digits = '0123456789'
    letters = 'abcdefghijklmnopqrstuvwxyz'

    digits_count = 0
    letters_count = 0

    for symbol in s:
        if symbol in digits:
            digits_count += 1

        if symbol.lower() in letters:
            letters_count += 1

    if digits_count > letters_count:
        return 'digits'
    elif digits_count < letters_count:
        return 'letters'

    return 'tie'

# print(digits_or_letters("abc123"))
# print(digits_or_letters("a1b2c3d"))
# print(digits_or_letters("1a2b3c4"))
# print(digits_or_letters("abc123!@#DEF"))
# print(digits_or_letters("H3110 W0R1D"))
# print(digits_or_letters("P455W0RD"))