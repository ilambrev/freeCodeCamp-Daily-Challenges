def rotate(matrix):
    rotated_matrix = []

    for i in range(len(matrix[0])):
        row = []

        for j in range(len(matrix) - 1, -1, -1):
            row.append(matrix[j][i])

        rotated_matrix.append(row)

    return rotated_matrix

# print(rotate([[1]]))
# print(rotate([[1, 2], [3, 4]]))
# print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]))