from string import digits, ascii_lowercase, ascii_uppercase

def check_strength(password):
    special_characters = "!@#$%^&*"
    has_proper_length = len(password) >= 8
    has_uppercase_letters = len([letter for letter in password if letter in ascii_uppercase]) > 0
    has_lowercase_letters = len([letter for letter in password if letter in ascii_lowercase]) > 0
    has_digits = len([digit for digit in password if digit in digits]) > 0
    has_special_characters = len([character for character in password if character in special_characters]) > 0
    conditions = [has_proper_length, has_uppercase_letters and has_lowercase_letters, has_digits, has_special_characters]

    met_conditions = len([condition for condition in conditions if condition])

    if met_conditions < 2:
        return "weak"
    elif met_conditions < 4:
        return "medium"
    else:
        return "strong"

# print(check_strength("123456"))
# print(check_strength("pass!!!"))
# print(check_strength("Qwerty"))
# print(check_strength("PASSWORD"))
# print(check_strength("PASSWORD!"))
# print(check_strength("PassWord%^!"))
# print(check_strength("qwerty12345"))
# print(check_strength("PASSWORD!"))
# print(check_strength("PASSWORD!"))
# print(check_strength("S3cur3P@ssw0rd"))
# print(check_strength("C0d3&Fun!"))