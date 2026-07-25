def find_signal(grid):
    coordinates = {}

    def find_coordinates(i, j, distance):
        if j + distance < len(grid[i]):
            coordinate = f"{i}-{j + distance}"
            coordinates[coordinate] = coordinates.get(coordinate, 0) + 1
        if j - distance >= 0:
            coordinate = f"{i}-{j - distance}"
            coordinates[coordinate] = coordinates.get(coordinate, 0) + 1
        if i + distance < len(grid):
            coordinate = f"{i + distance}-{j}"
            coordinates[coordinate] = coordinates.get(coordinate, 0) + 1
        if i - distance >= 0:
            coordinate = f"{i - distance}-{j}"
            coordinates[coordinate] = coordinates.get(coordinate, 0) + 1
        if i - distance >= 0 and j + distance < len(grid[i]):
            coordinate = f"{i - distance}-{j + distance}"
            coordinates[coordinate] = coordinates.get(coordinate, 0) + 1
        if i + distance < len(grid) and j + distance < len(grid[i]):
            coordinate = f"{i + distance}-{j + distance}"
            coordinates[coordinate] = coordinates.get(coordinate, 0) + 1
        if i + distance < len(grid) and j - distance >= 0:
            coordinate = f"{i + distance}-{j - distance}"
            coordinates[coordinate] = coordinates.get(coordinate, 0) + 1
        if i - distance >= 0 and j - distance >= 0:
            coordinate = f"{i - distance}-{j - distance}"
            coordinates[coordinate] = coordinates.get(coordinate, 0) + 1

    def find_phone_coordiate():
        coordinate = ""
        max_repeats = 0
        for key, value in coordinates.items():
            if value > max_repeats:
                coordinate = key
                max_repeats = value

        return [int(d) for d in coordinate.split("-")]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 0:
                find_coordinates(i, j, grid[i][j])

    return find_phone_coordiate()

# print(find_signal([[0, 0, 1], [0, 1, 0], [0, 0, 1]]))
# print(find_signal([[0, 2, 0], [1, 0, 0], [0, 0, 1]]))
# print(find_signal([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]]))
# print(find_signal([[0, 3, 0, 0, 0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 0], [4, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
# print(find_signal([[3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 2]]))