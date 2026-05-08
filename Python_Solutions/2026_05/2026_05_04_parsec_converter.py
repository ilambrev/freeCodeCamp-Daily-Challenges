def convert_parsecs(parsecs):
    hours = 2
    light_years = 6

    if parsecs % 2 == 0:
        return int((parsecs / 2) * light_years)
    else:
        return parsecs * hours

# print(convert_parsecs(1))
# print(convert_parsecs(2))
# print(convert_parsecs(31))
# print(convert_parsecs(88))
# print(convert_parsecs(17))
# print(convert_parsecs(14))