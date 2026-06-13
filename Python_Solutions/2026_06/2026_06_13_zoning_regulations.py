def get_zone_violations(grid):
    labels = {
        "i": ["R", "I"],
        "A": ["C"],
        "R": ["i", "C"],
        "I": ["i"],
        "C": ["R", "A"],
        "": []
    }

    violation_coordinates = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            label = grid[i][j]
            constraints = labels[label]

            if i > 0 and grid[i-1][j] in constraints:
                violation_coordinates.append([i, j])
                continue
            if i < len(grid) - 1 and grid[i+1][j] in constraints:
                violation_coordinates.append([i, j])
                continue
            if j > 0 and grid[i][j-1] in constraints:
                violation_coordinates.append([i, j])
                continue
            if j < len(grid[i]) - 1 and grid[i][j+1] in constraints:
                violation_coordinates.append([i, j])
                continue

    return violation_coordinates

# print(get_zone_violations([["R", "C"], ["", "C"]]))
# print(get_zone_violations([["", "i"], ["", "R"], ["R", "I"]]))
# print(get_zone_violations([["A", "i", "C"], ["A", "", "C"], ["R", "R", "I"]]))
# print(get_zone_violations([["R", "R", "C", "R", "R"], ["R", "I", "C", "", "A"], ["R", "R", "", "i", "A"]]))
# print(get_zone_violations([["R", "A", "A", "", "i", "i"], ["R", "I", "", "C", "i", "i"], ["R", "", "C", "C", "A", "A"], ["R", "R", "C", "I", "R", "R"]]))