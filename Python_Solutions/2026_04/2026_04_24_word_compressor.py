def compress(s):
    unique_words = {}
    text_as_words = s.split()
    compressed_words = []

    for i in range(len(text_as_words)):
        word = text_as_words[i]
        index = 0

        if word in unique_words:
            index = unique_words[word]

        if index > 0:
            compressed_words.append(str(index))
        else:
            unique_words[word] = i + 1
            compressed_words.append(word)

    return " ".join(compressed_words)

# print(compress("practice makes perfect and perfect practice makes perfect"))
# print(compress("hello hello hello"))
# print(compress("the cat sat on the mat on which the cat sat"))
# print(compress("the more you know the more you realize you don't know"))
# print(compress("lorem ipsum dolor sit per elit donec sit nostra libero per donec ligula sit gravida at elit vitae a elit sodales donec en donec at dolor nam ligula dignissim risus at ligula per nam ipsum ipsum gravida en elit per ipsum ligula en gravida per sodales sit at nam lorem sit per libero en ipsum elit sit sodales sit risus elit risus ipsum elit at gravida vitae en dignissim nam sit vitae sollicitudin per nostra per sit libero"))