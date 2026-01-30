def find_pawn_moves(position):
    row = int(position[1])

    if row == 2:
        return [position[0] + str(row + 1), position[0] + str(row + 2)]
    elif row == 8:
        return []
    else:
        return [position[0] + str(row + 1)]

# print(find_pawn_moves("D4"))
# print(find_pawn_moves("B2"))
# print(find_pawn_moves("A7"))
# print(find_pawn_moves("G2"))
# print(find_pawn_moves("E3"))