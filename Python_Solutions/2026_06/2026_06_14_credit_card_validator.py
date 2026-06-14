def is_valid_card(number):
    sum = int(number[-1])

    digits = number[::-1][1:]

    for i in range(len(digits)):
        number = int(digits[i])

        if i % 2 == 0:
            number *= 2

        if number > 9:
            number -= 9

        sum += number

    return sum % 10 == 0

# print(is_valid_card("4532015112830366"))
# print(is_valid_card("5425233430109903"))
# print(is_valid_card("371449635398431"))
# print(is_valid_card("6011111111111117"))
# print(is_valid_card("4532015112830367"))
# print(is_valid_card("1234567890123456"))
# print(is_valid_card("4532015112830368"))