def rook_bishop_attack(rook, bishop):
    letters = "ABCDEFGH"
    rook_col = rook[:1]
    rook_row = rook[1:]
    bishop_col = bishop[:1]
    bishop_row = bishop[1:]

    if rook_col == bishop_col or rook_row == bishop_row:
        return "rook"
    elif abs(letters.find(bishop_col) - letters.find(rook_col)) == abs(int(bishop_row) - int(rook_row)):
        return "bishop"
    else:
        return "neither"

# print(rook_bishop_attack("A1", "A5"))
# print(rook_bishop_attack("C3", "F6"))
# print(rook_bishop_attack("D4", "D7"))
# print(rook_bishop_attack("B7", "H1"))
# print(rook_bishop_attack("B3", "C5"))
# print(rook_bishop_attack("G3", "E8"))