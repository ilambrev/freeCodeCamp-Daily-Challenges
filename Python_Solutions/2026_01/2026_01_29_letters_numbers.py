from string import ascii_letters, digits

def separate_letters_and_numbers(s):

    return "".join(["-" + s[i] if i > 0 and (s[i-1] in ascii_letters and s[i] not in ascii_letters
                    or s[i-1] in digits and s[i] not in digits)
                    else s[i] for i in range(len(s))])

# print(separate_letters_and_numbers("ABC123"))
# print(separate_letters_and_numbers("Route66"))
# print(separate_letters_and_numbers("H3LL0W0RLD"))
# print(separate_letters_and_numbers("a1b2c3d4"))