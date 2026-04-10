def rook_attack(rook1, rook2):
    letter1 = rook1[:1]
    number1 = rook1[1:]
    letter2 = rook2[:1]
    number2 = rook2[1:]

    if letter1 == letter2 and not number1 == number2:
        return True
    elif not letter1 == letter2 and number1 == number2:
        return True
    else:
        return False

# print(rook_attack("A1", "A8"))
# print(rook_attack("B4", "F4"))
# print(rook_attack("E3", "D4"))
# print(rook_attack("H7", "F6"))