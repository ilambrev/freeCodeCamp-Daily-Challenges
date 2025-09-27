def jbelmu(text):
    words = text.split()

    for i in range(len(words)):
        if len(words[i]) > 3:
            words[i] = (words[i][0] 
                        + ''.join(sorted([letter for letter in words[i][1:-1]])) 
                        + words[i][-1])

    return ' '.join(words)

# print(jbelmu("hello world"))
# print(jbelmu("i love jumbled text"))
# print(jbelmu("freecodecamp is my favorite place to learn to code"))
# print(jbelmu("the quick brown fox jumps over the lazy dog"))