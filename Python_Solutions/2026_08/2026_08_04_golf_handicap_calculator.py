from math import ceil

def calculate_handicap(scores, pars):

    return ceil(sum([scores[i] - pars[i] for i in range(len(scores))]) / len(scores) * 10) / 10

# print(calculate_handicap([72, 72, 72], [72, 72, 72]))
# print(calculate_handicap([80, 76, 78, 78], [72, 72, 72, 72]))
# print(calculate_handicap([42, 45, 46, 44], [36, 36, 36, 36]))
# print(calculate_handicap([85, 80, 76, 79, 82], [72, 72, 72, 71, 71]))
# print(calculate_handicap([41, 50, 48, 52, 46, 49], [35, 37, 35, 37, 35, 37]))