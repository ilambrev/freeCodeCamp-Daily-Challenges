def get_bingo_letter(n):
    thresholds = [15, 30, 45, 60, 75]
    letters = ["B", "I", "N", "G", "O"]

    for i in range(len(thresholds)):
        if n <= thresholds[i]:
            return letters[i]
    
    return n

# print(get_bingo_letter(75))
# print(get_bingo_letter(54))
# print(get_bingo_letter(25))
# print(get_bingo_letter(38))
# print(get_bingo_letter(11))