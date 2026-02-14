def get_difficulty(track):
    points = 0
    last_direction = "S"

    for direction in track:
        if direction == "L" or direction == "R":
            if last_direction == "L" or last_direction == "R" and not direction == last_direction:
                points += 15
            else:
                points += 5

        last_direction = direction

    if points <= 100:
        return "Easy"
    elif points <= 200:
        return "Medium"
    else:
        return "Hard"

# print(get_difficulty("SLSLLSRRLSRLRL"))
# print(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"))
# print(get_difficulty("SRRRRLSLLRLRSSRLSRL"))
# print(get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL"))
# print(get_difficulty("SLLSSLRLSLSLRSLSSLRL"))
# print(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"))