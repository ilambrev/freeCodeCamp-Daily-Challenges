def get_odds(dice, target):
    combinations = 6**dice
    table = [[0 for _ in range(target + 1)] for _ in range(dice + 1)]
    for i in range(1, target + 1):
        table[0][i] = i

    for i in range(1, min(6 + 1, target + 1)):
        table[1][i] = 1

    for i in range(2, len(table)):
        cols = min(i * 6, len(table[i]) - 1)
        for j in range(1, cols + 1):
            col_value = sum(table[i-1][max(0, j-6):j])
            table[i][j] = col_value

    odds = round(combinations / table[dice][target])

    return f"1 in {odds}"

# print(get_odds(1, 5))
# print(get_odds(2, 4))
# print(get_odds(3, 10))
# print(get_odds(4, 7))
# print(get_odds(5, 26))
# print(get_odds(6, 35))