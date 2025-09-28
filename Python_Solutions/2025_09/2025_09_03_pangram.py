from string import ascii_lowercase

def is_pangram(sentence, letters):
    sentence_letters = {}

    for letter in sentence:
        if letter.lower() in ascii_lowercase and not letter in sentence_letters:
            sentence_letters[letter.lower()] = 0

    for letter in letters:
        if not letter in sentence_letters:
            return False
        
        sentence_letters[letter] += 1

    return len([letter for letter in sentence_letters if sentence_letters[letter] == 0]) == 0

# print(is_pangram("hello", "helo"))
# print(is_pangram("hello", "hel"))
# print(is_pangram("hello", "helow"))
# print(is_pangram("hello world", "helowrd"))
# print(is_pangram("Hello World!", "helowrd"))
# print(is_pangram("Hello World!", "heliowrd"))
# print(is_pangram("freeCodeCamp", "frcdmp"))
# print(is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz"))