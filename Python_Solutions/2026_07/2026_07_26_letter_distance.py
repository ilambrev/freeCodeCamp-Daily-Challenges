from string import ascii_lowercase

def letter_distance(str1, str2):
    alphabet_letters = 26
    distance = 0

    for i in range(len(str1)):
        index1 = ascii_lowercase.find(str1[i])
        index2 = ascii_lowercase.find(str2[i])

        dif = abs(index1 - index2)
        distance += min(dif, alphabet_letters - dif)

    return distance

# print(letter_distance("abc", "bcd"))
# print(letter_distance("abc", "xyz"))
# print(letter_distance("encrypt", "decrypt"))
# print(letter_distance("algorithm", "codeblock"))
# print(letter_distance("lobster", "penguin"))
# print(letter_distance("alligator", "crocodile"))