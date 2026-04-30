def is_in_crossword(char):
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0]
    ]
    binary_strings = []

    for row in grid:
        left_to_right = "".join(str(digit) for digit in row)
        right_to_left = left_to_right[::-1]
        binary_strings += [left_to_right, right_to_left]

    for i in range(len(grid[0])):
        col = []
        for j in range(len(grid)):
            col.append(grid[j][i])
        up_to_down = "".join(str(digit) for digit in col)
        down_to_up = up_to_down[::-1]
        binary_strings += [up_to_down, down_to_up]

    char_binary = format(ord(char), "b")
    char_binary = (8 - len(char_binary)) * "0" + char_binary

    return char_binary in binary_strings

# print(is_in_crossword("I"))
# print(is_in_crossword("D"))
# print(is_in_crossword("0"))
# print(is_in_crossword("u"))
# print(is_in_crossword("Y"))
# print(is_in_crossword("p"))
# print(is_in_crossword("1"))
# print(is_in_crossword("Q"))