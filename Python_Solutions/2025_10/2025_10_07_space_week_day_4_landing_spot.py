def find_landing_spot(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    safest_spot_value = 0
    lowest_total_danger = 36
    safest_spot_row = 0
    safest_spot_col = 0

    for i in range(rows):
        for j in range(cols):
            spot = matrix[i][j]

            if spot == safest_spot_value:
                surrounding_cells_danger = 0

                if i > 0:
                    surrounding_cells_danger += matrix[i - 1][j]
                if i < rows - 1:
                    surrounding_cells_danger += matrix[i + 1][j]
                if j > 0:
                    surrounding_cells_danger += matrix[i][j - 1]
                if j < cols - 1:
                    surrounding_cells_danger += matrix[i][j + 1]

                if surrounding_cells_danger < lowest_total_danger:
                    lowest_total_danger = surrounding_cells_danger
                    safest_spot_row = i
                    safest_spot_col = j

    return [safest_spot_row, safest_spot_col]

# print(find_landing_spot([[1, 0], [2, 0]]))
# print(find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]))
# print(find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]))
# print(find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]))