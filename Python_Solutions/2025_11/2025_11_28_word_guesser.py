def compare(word, guess):
    letters = {}
    result = ["0"] * len(word)

    for letter in word:
        if not letter in letters:
            letters[letter] = 0

        letters[letter] += 1

    for i in range(len(guess)):
        if guess[i] == word[i]:
            result[i] = str(2)
            letters[guess[i]] -= 1

    for i in range(len(guess)):
        if guess[i] in letters and letters[guess[i]] > 0 and not guess[i] == word[i]:
            result[i] = str(1)
            letters[guess[i]] -= 1

    return "".join(result)

# print(compare("APPLE", "POPPA"))
# print(compare("REACT", "TRACE"))
# print(compare("DEBUGS", "PYTHON"))
# print(compare("JAVASCRIPT", "TYPESCRIPT"))
# print(compare("ORANGE", "ROUNDS"))
# print(compare("WIRELESS", "ETHERNET"))