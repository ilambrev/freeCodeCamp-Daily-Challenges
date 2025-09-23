def is_mirror(str1, str2):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    str1_letters_reverse = ''.join(
        [letter for letter in str1 if letter.lower() in letters][::-1])
    str2_letters = ''.join(
        [letter for letter in str2 if letter.lower() in letters])

    return str1_letters_reverse == str2_letters

# print(is_mirror("helloworld", "helloworld"))
# print(is_mirror("Hello World", "dlroW olleH"))
# print(is_mirror("RaceCar", "raCecaR"))
# print(is_mirror("RaceCar", "RaceCar"))
# print(is_mirror("Mirror", "rorrim"))
# print(is_mirror("Hello World", "dlroW-olleH"))
# print(is_mirror("Hello World", "!dlroW !olleH"))