def parse_roman_numeral(numeral):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    decimal_number = 0
    buffer = roman_dict[numeral[0]]

    for i in range(1, len(numeral)):
        if roman_dict[numeral[i]] > roman_dict[numeral[i - 1]]:
            decimal_number += roman_dict[numeral[i]] - buffer
            buffer = 0
        else:
            decimal_number += buffer
            buffer = 0
            buffer += roman_dict[numeral[i]]

    return decimal_number + buffer

# print(parse_roman_numeral("III"))
# print(parse_roman_numeral("IV"))
# print(parse_roman_numeral("XXVI"))
# print(parse_roman_numeral("XCIX"))
# print(parse_roman_numeral("CDLX"))
# print(parse_roman_numeral("DIV"))
# print(parse_roman_numeral("MMXXV"))