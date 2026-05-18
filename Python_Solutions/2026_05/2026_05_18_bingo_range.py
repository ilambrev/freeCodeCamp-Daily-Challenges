def get_bingo_range(letter):
    bingo_letters = {
        "B": (1, 15),
        "I": (16, 30),
        "N": (31, 45),
        "G": (46, 60),
        "O": (61, 75)
    }

    bingo_range = []

    if letter in bingo_letters:
        lower_limit, upper_limit = bingo_letters[letter]
        bingo_range = [n for n in range(lower_limit, upper_limit + 1)]

    return bingo_range

# print(get_bingo_range("B"))
# print(get_bingo_range("I"))
# print(get_bingo_range("N"))
# print(get_bingo_range("G"))
# print(get_bingo_range("O"))