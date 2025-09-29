def repeat_vowels(s):
    vowels = 'aeiou'
    counter = 0

    letters = []

    for letter in s:
        if letter.lower() in vowels:
            letters.append(letter + letter.lower() * counter)
            counter += 1
        else:
            letters.append(letter)

    return ''.join(letters)

# print(repeat_vowels("hello world"))
# print(repeat_vowels("freeCodeCamp"))
# print(repeat_vowels("AEIOU"))
# print(repeat_vowels("I like eating ice cream in Iceland"))