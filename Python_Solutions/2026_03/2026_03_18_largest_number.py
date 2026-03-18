def largest_number(s):
    separators = {",": " ", "!": " ", "?": " ", ":": " ", ";": " "}
    s = s.translate(str.maketrans(separators))
    largest_number = max(float(n) for n in s.split())

    return int(largest_number) if largest_number.is_integer() else largest_number

# print(largest_number("1,2"))
# print(largest_number("4;15:60,26?52!0"))
# print(largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011"))
# print(largest_number("12;-50,99.9,49.1!-10.1?88?16"))