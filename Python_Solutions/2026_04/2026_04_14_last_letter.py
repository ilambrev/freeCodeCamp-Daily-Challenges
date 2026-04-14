from string import ascii_lowercase

def get_last_letter(s):
    last_letter_index = 0
    last_letter = s[0]

    for letter in s:
        index = ascii_lowercase.find(letter.lower())
        if index > last_letter_index:
            last_letter_index = index
            last_letter = letter

    return last_letter

# print(get_last_letter("world"))
# print(get_last_letter("Hello World"))
# print(get_last_letter("The quick brown fox jumped over the lazy dog."))
# print(get_last_letter("HeLl0"))
# print(get_last_letter("!#$ er@R asd fT.,> 2t0e9"))