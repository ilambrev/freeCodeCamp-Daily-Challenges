def get_next_bingo_number(n):
    numbers_ranges = ["B", 15, "I", 30, "N", 45, "G", 60, "O", 75]
    letter = n[:1]
    number = int(n[1:])

    letter_index = numbers_ranges.index(letter)
    number = number + 1
    
    if number > 75:
        number = 1
        letter = numbers_ranges[0]
    elif number > numbers_ranges[letter_index+1]:
        letter = numbers_ranges[letter_index+2]

    return f"{letter}{number}"

# print(get_next_bingo_number("B10"))
# print(get_next_bingo_number("N33"))
# print(get_next_bingo_number("I30"))
# print(get_next_bingo_number("G60"))
# print(get_next_bingo_number("O75"))