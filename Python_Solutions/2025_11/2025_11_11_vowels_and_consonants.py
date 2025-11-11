from string import ascii_letters

def count(s):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    other_letters_count = 0

    for letter in s:
        if letter in vowels:
            vowels_count += 1
        elif letter in ascii_letters:
            other_letters_count += 1

    return [vowels_count, other_letters_count]

# print(count("Hello World"))
# print(count("JavaScript"))
# print(count("Python"))
# print(count("freeCodeCamp"))
# print(count("Hello, World!"))
# print(count("The quick brown fox jumps over the lazy dog."))