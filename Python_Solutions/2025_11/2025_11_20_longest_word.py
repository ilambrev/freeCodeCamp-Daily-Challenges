from string import ascii_letters, punctuation

def longest_word(sentence):
    words = sentence.split()

    longest_word = ""
    longest_word_length = 0

    for word in words:
        letters_count = len([letter for letter in word if letter in ascii_letters])

        if letters_count > longest_word_length:
            longest_word = word
            longest_word_length = letters_count

    return "".join([letter for letter in longest_word if not letter in punctuation])

# print(longest_word("The quick red fox"))
# print(longest_word("Hello coding challenge."))
# print(longest_word("Do Try This At Home."))
# print(longest_word("This sentence... has commas, ellipses, and an exlamation point!"))
# print(longest_word("A tie? No way!"))
# print(longest_word("Wouldn't you like to know."))