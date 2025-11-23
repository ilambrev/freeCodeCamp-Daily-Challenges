from string import ascii_lowercase

def count_characters(sentence):
    letters = [[letter, 0] for letter in ascii_lowercase]
    for letter in sentence:
        index = -1

        if letter.lower() in ascii_lowercase:
            index = ascii_lowercase.find(letter.lower())
            letters[index][1] += 1

    return [f"{a[0]} {a[1]}" for a in letters if a[1] > 0]

# print(count_characters("hello world"))
# print(count_characters("I love coding challenges!"))
# print(count_characters("// TODO: Complete this challenge ASAP!"))