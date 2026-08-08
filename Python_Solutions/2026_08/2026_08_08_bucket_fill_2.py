def bucket_fill(grid, target_color):
    def calculate_clicks(grid, point):
        counter = 1
        row = point[0]
        col = point[1]
        color = grid[row][col]

        if row > 0 and grid[row-1][col] == color:
            counter += 1
        if row > 0 and col < len(grid[row]) - 1 and grid[row-1][col+1] == color:
            counter += 1
        if col < len(grid[row]) - 1 and grid[row][col+1] == color:
            counter += 1
        if row < len(grid) - 1 and col < len(grid[row]) - 1 and grid[row+1][col+1] == color:
            counter += 1
        if row < len(grid) - 1 and grid[row+1][col] == color:
            counter += 1
        if row < len(grid) - 1 and col > 0 and grid[row+1][col-1] == color:
            counter += 1
        if col > 0 and grid[row][col-1] == color:
            counter += 1
        if row > 0 and col > 0 and grid[row-1][col-1] == color:
            counter += 1

        return counter

    def find_points_neighbors(grid, target_color):
        points = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not grid[i][j] == target_color:
                    points[f"{i}:{j}"] = calculate_clicks(grid, [i, j])

        return points

    def get_point_with_max_neighbors_to_fill(points):
        points_coordinates = [k for k, v in sorted(points.items(), key=lambda item: (-item[1]))]
        x, y = points_coordinates[0].split(":")

        return [int(x), int(y)]

    def fill_neighbours(grid, target_color, point):
        row = point[0]
        col = point[1]
        color = grid[row][col]
        grid[row][col] = target_color

        if row > 0 and grid[row-1][col] == color:
            grid[row-1][col] = target_color
        if row > 0 and col < len(grid[row]) - 1 and grid[row-1][col+1] == color:
            grid[row-1][col+1] = target_color
        if col < len(grid[row]) - 1 and grid[row][col+1] == color:
            grid[row][col+1] = target_color
        if row < len(grid) - 1 and col < len(grid[row]) - 1 and grid[row+1][col+1] == color:
            grid[row+1][col+1] = target_color
        if row < len(grid) - 1 and grid[row+1][col] == color:
            grid[row+1][col] = target_color
        if row < len(grid) - 1 and col > 0 and grid[row+1][col-1] == color:
            grid[row+1][col-1] = target_color
        if col > 0 and grid[row][col-1] == color:
            grid[row][col-1] = target_color
        if row > 0 and col > 0 and grid[row-1][col-1] == color:
            grid[row-1][col-1] = target_color

    counter = 0

    while True:
        points = find_points_neighbors(grid, target_color)
        if len(points) > 0:
            counter += 1
            point = get_point_with_max_neighbors_to_fill(points)
            fill_neighbours(grid, target_color, point)
        else:
            break

    return counter

# print(bucket_fill([["R", "R"], ["R", "R"]], "G"))
# print(bucket_fill([["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]], "B"))
# print(bucket_fill([["G", "Y", "Y"], ["G", "Y", "G"], ["Y", "Y", "G"]], "R"))
# print(bucket_fill([["G", "G", "P", "Y"], ["O", "P", "P", "P"], ["O", "O", "P", "G"], ["G", "O", "O", "G"]], "P"))
# print(bucket_fill([["G", "G", "C", "C", "O"], ["B", "Y", "B", "Y", "O"], ["B", "J", "O", "J", "B"], ["G", "Y", "Y", "Y", "B"], ["G", "P", "P", "G", "G"]], "Y"))