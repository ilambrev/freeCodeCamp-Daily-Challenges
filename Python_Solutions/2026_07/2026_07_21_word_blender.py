def blend_words(word1, word2):
    i1 = int(len(word1) / 2)
    i2 = int(len(word2) / 2)

    return f"{word1[:i1]}{word2[i2:]}"

# print(blend_words("turtle", "toucan"))
# print(blend_words("chipmunk", "flamingo"))
# print(blend_words("falcon", "pelican"))
# print(blend_words("hyena", "iguana"))
# print(blend_words("scorpion", "gorilla"))
# print(blend_words("platypus", "wolverine"))