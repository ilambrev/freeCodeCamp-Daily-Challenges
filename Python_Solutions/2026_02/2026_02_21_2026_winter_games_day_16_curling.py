def score_curling(house):
    empty_space = "."
    red_stone = "R"
    yellow_stone = "Y"
    button = "22"
    ring_1 = ["11", "12", "13", "21", "23", "31", "32", "33"]
    ring_2 = ["00", "01", "02", "03", "04", "10", "14", "20", "24", "30", "34", "40", "41", "42", "43", "44"]
    red_player_scores = [0, 0, 0]
    yellow_player_scores = [0, 0, 0]

    for i in range(len(house)):
        for j in range(len(house[i])):
            position = str(i) + str(j)
            if house[i][j] == red_stone:
                if position == button:
                    red_player_scores[0] += 1
                elif position == position in ring_1:
                    red_player_scores[1] += 1
                elif position in ring_2:
                    red_player_scores[2] += 1
            if house[i][j] == yellow_stone:
                if position == button:
                    yellow_player_scores[0] += 1
                elif position == position in ring_1:
                    yellow_player_scores[1] += 1
                elif position in ring_2:
                    yellow_player_scores[2] += 1
    
    scores = 0

    if red_player_scores[0] > yellow_player_scores[0]:
        scores += red_player_scores[0]
        if yellow_player_scores[1] == 0:
            scores += red_player_scores[1]
            if yellow_player_scores[2] == 0:
                scores += red_player_scores[2]
        return f"R: {scores}"
    elif yellow_player_scores[0] > red_player_scores[0]:
        scores += yellow_player_scores[0]
        if red_player_scores[1] == 0:
            scores += yellow_player_scores[1]
            if red_player_scores[2] == 0:
                scores += yellow_player_scores[2]
        return f"Y: {scores}"
    elif red_player_scores[1] > 0 and yellow_player_scores[1] == 0:
        scores += red_player_scores[1]
        if yellow_player_scores[2] == 0:
            scores += red_player_scores[2]
        return f"R: {scores}"
    elif yellow_player_scores[1] > 0 and red_player_scores[1] == 0:
        scores += yellow_player_scores[1]
        if red_player_scores[2] == 0:
            scores += yellow_player_scores[2]
        return f"Y: {scores}"
    elif red_player_scores[2] > 0 and yellow_player_scores[2] == 0:
        scores += red_player_scores[2]
        return f"R: {scores}"
    elif yellow_player_scores[2] > 0 and red_player_scores[2] == 0:
        scores += yellow_player_scores[2]
        return f"Y: {scores}"

    return "No points awarded"

# print(score_curling([[".", ".", "R", ".", "."], [".", "R", ".", ".", "."], ["Y", ".", ".", ".", "."], [".", "R", ".", ".", "."], [".", ".", ".", ".", "."]]))
# print(score_curling([[".", ".", "R", ".", "."], [".", ".", ".", ".", "."], [".", ".", "Y", ".", "R"], [".", ".", "Y", "Y", "."], [".", "Y", "R", "R", "."]]))
# print(score_curling([[".", "R", "Y", ".", "."], ["Y", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", "Y", "R", "Y", "."], [".", ".", "R", "R", "."]]))
# print(score_curling([[".", "Y", "Y", ".", "."], ["Y", ".", ".", "R", "."], [".", ".", "R", ".", "."], [".", ".", "R", "R", "."], [".", "Y", "R", "Y", "."]]))
# print(score_curling([["Y", "Y", "Y", "Y", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "R", "Y", "R", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "Y", "Y", "Y", "Y"]]))
# print(score_curling([["Y", "R", "Y", "R", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", ".", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", "R", "Y"]]))