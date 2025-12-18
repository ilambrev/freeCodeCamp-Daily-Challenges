def create_board(dimensions):
    characters = ["X", "O"]
    board = []
    current_char_index = 0

    for i in range(dimensions[0]):
        row = []

        for j in range(dimensions[1]):
            row.append(characters[current_char_index])
            current_char_index = abs(current_char_index - 1)

        if dimensions[1] % 2 == 0:
            current_char_index = abs(current_char_index - 1)
        
        board.append(row)

    return board

# print(create_board([3, 3]))
# print(create_board([6, 1]))
# print(create_board([2, 10]))
# print(create_board([5, 4]))