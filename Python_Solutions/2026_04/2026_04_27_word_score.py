from string import ascii_uppercase

def get_word_score(word):

    return sum(ascii_uppercase.find(letter.upper()) + 1 for letter in word)

# print(get_word_score("hi"))
# print(get_word_score("hello"))
# print(get_word_score("hippopotamus"))
# print(get_word_score("freeCodeCamp"))