def transpose(matrix):
    transposed_matrix = []

    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transposed_matrix.append(row)

    return transposed_matrix

# print(transpose([[1, 2, 3], [4, 5, 6]]))
# print(transpose([[1, 2], [3, 4], [5, 6]]))
# print(transpose([[1, 2], [3, 4], [5, 6], [7, 8]]))
# print(transpose([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]]))
# print(transpose([[True, False, True, False], [False, True, False, True], [True, True, False, False], [False, False, True, True], [True, False, False, True]]))