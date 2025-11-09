def find_word(matrix, word):
    for i in range(len(matrix)):
        row_as_string = "".join(matrix[i])
        word_index = row_as_string.find(word)

        if word_index > -1:
            return [[i, word_index], [i, word_index + len(word) - 1]]

        word_index = row_as_string[::-1].find(word)

        if word_index > -1:
            word_index = abs(word_index - (len(row_as_string) - 1))
            return [[i, word_index], [i, word_index - (len(word) - 1)]]

    for i in range(len(matrix[0])):
        col_chars = []

        for j in range(len(matrix)):
            col_chars.append(matrix[j][i])

        col_as_string = "".join(col_chars)
        word_index = col_as_string.find(word)

        if word_index > -1:
            return [[word_index, i], [word_index + len(word) - 1, i]]

        word_index = col_as_string[::-1].find(word)

        if word_index > -1:
            word_index = abs(word_index - (len(row_as_string) - 1))
            return [[word_index, i], [word_index - (len(word) - 1), i]]

    return []

# print(find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat"))
# print(find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog"))
# print(find_word([["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish"))
# print(find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox"))