def is_valid_domino_chain(dominoes):
    is_valid = True

    for i in range(1, len(dominoes)):
        if not dominoes[i][0] == dominoes[i-1][1]:
            is_valid = False
            break

    return is_valid

# print(is_valid_domino_chain([[1, 3], [3, 6], [6, 5]]))  # should return True
# print(is_valid_domino_chain([[6, 2], [3, 4], [4, 1]]))  # should return False
# print(is_valid_domino_chain([[2, 5], [5, 6], [5, 1]]))  # should return False
# print(is_valid_domino_chain([[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]]))  # should return True
# print(is_valid_domino_chain([[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]]))  # should return False