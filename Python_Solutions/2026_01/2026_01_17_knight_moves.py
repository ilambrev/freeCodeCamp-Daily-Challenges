def knight_moves(position):
    rows = "87654321"
    cols = "ABCDEFGH"
    max_row = 7
    max_col = 7

    col = cols.find(position[0])
    row = rows.find(position[1])

    possible_moves = 0

    if row - 2 >= 0 and col - 1 >= 0:
        possible_moves += 1

    if row - 2 >= 0 and col + 1 <= max_col:
        possible_moves += 1

    if row + 2 <= max_row and col - 1 >= 0:
        possible_moves += 1

    if row + 2 <= max_row and col + 1 <= max_col:
        possible_moves += 1

    if row + 1 <= max_row and col + 2 <= max_col:
        possible_moves += 1

    if row - 1 >= 0 and col + 2 <= max_col:
        possible_moves += 1

    if row + 1 <= max_row and col - 2 >= 0:
        possible_moves += 1

    if row - 1 >= 0 and col - 2 >= 0:
        possible_moves += 1

    return possible_moves

# print(knight_moves("A1"))
# print(knight_moves("D4"))
# print(knight_moves("G6"))
# print(knight_moves("B8"))
# print(knight_moves("H3"))