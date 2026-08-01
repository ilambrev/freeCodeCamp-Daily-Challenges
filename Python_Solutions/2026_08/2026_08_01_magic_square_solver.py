def solve_magic_square(grid):
    rows = 3
    cols = 3
    sums = {}

    for row in grid:
        current_sum = sum(row)
        sums[current_sum] = sums.get(current_sum, 0) + 1

    for i in range(cols):
        current_sum = 0
        for j in range(rows):
            current_sum += grid[j][i]
        sums[current_sum] = sums.get(current_sum, 0) + 1

    right_diag_sum = grid[0][0] + grid[1][1] + grid[2][2]
    sums[right_diag_sum] = sums.get(right_diag_sum, 0) + 1

    left_diag_sum = grid[2][0] + grid[1][1] + grid[0][2]
    sums[left_diag_sum] = sums.get(left_diag_sum, 0) + 1

    return "impossible" if len(sums) > 2 else max(sums.keys()) - min(sums.keys())

# print(solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]))
# print(solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]))
# print(solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]))
# print(solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]))
# print(solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]))