def get_words(paragraph):
    punctuation_signs = [',', '.', '!']
    words = [word.lower() for word in paragraph.split() if not word in punctuation_signs]
    words_dict = {}

    for word in words:
        if word[-1] in punctuation_signs:
            word = word[:-1]

        if not word in words_dict:
            words_dict[word] = 0
        
        words_dict[word] += 1

    return [word for word in {k: v for k, v in sorted(words_dict.items(), key=lambda item: item[1], reverse=True)}][0:3]

# print(get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding"))
# print(get_words("I like coding. I like testing. I love debugging!"))
# print(get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!"))