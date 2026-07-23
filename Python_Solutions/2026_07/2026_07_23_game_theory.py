def play_game(p1, p2):
    p1_scores = 0
    p2_scores = 0

    for i in range(len(p1)):
        p1_strategy = p1[i]
        p2_strategy = p2[i]

        if p1_strategy == "C" and p2_strategy == "C":
            p1_scores += 3
            p2_scores += 3
        elif p1_strategy == "D" and p2_strategy == "D":
            p1_scores += 1
            p2_scores += 1
        elif p1_strategy == "C" and p2_strategy == "D":
            p2_scores += 5
        elif p2_strategy == "C" and p1_strategy == "D":
            p1_scores += 5

    return [p1_scores, p2_scores]

# print(play_game("CCCC", "CCCC"))  # should return [12, 12]
# print(play_game("DDDD", "DDDD"))  # should return [4, 4]
# print(play_game("CCDD", "CDDD"))  # should return [5, 10]
# print(play_game("CCCDCDCCCDDC", "CCDDCDCDDCCD"))  # should return [24, 34]
# print(play_game("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC"))  # should return [66, 21]