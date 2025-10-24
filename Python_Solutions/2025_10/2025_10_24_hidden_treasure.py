def dive(map, coordinates):
    target = map[coordinates[0]][coordinates[1]]

    if target == "-":
        return "Empty"

    not_found_parts = 0

    if map[coordinates[0]][coordinates[1]] == "O":
        not_found_parts += 1

    for i in range(8):
        current_row = coordinates[0]
        current_col = coordinates[1]

        if i == 0:
            current_row -= 1

            while current_row >= 0 and not map[current_row][current_col] == "-":
                if map[current_row][current_col] == "O":
                    not_found_parts += 1
                current_row -= 1

        if i == 1:
            current_row -= 1
            current_col += 1

            while current_row >= 0 and current_col < len(map[current_row]) and not map[current_row][current_col] == "-":
                if map[current_row][current_col] == "O":
                    not_found_parts += 1
                current_row -= 1
                current_col += 1

        if i == 2:
            current_col += 1

            while current_col < len(map[current_row]) and not map[current_row][current_col] == "-":
                if map[current_row][current_col] == "O":
                    not_found_parts += 1
                current_col += 1

        if i == 3:
            current_row += 1
            current_col += 1

            while current_row < len(map) and current_col < len(map[current_row]) and not map[current_row][current_col] == "-":
                if map[current_row][current_col] == "O":
                    not_found_parts += 1
                current_row += 1
                current_col += 1

        if i == 4:
            current_row += 1

            while current_row < len(map) and not map[current_row][current_col] == "-":
                if map[current_row][current_col] == "O":
                    not_found_parts += 1
                current_row += 1

        if i == 5:
            current_row += 1
            current_col -= 1

            while current_row < len(map) and current_col >= 0 and not map[current_row][current_col] == "-":
                if map[current_row][current_col] == "O":
                    not_found_parts += 1
                current_row += 1
                current_col -= 1

        if i == 6:
            current_col -= 1

            while current_col >= 0 and not map[current_row][current_col] == "-":
                if map[current_row][current_col] == "O":
                    not_found_parts += 1
                current_col -= 1

        if i == 7:
            current_row -= 1
            current_col -= 1

            while current_row >= 0 and current_col >= 0 and not map[current_row][current_col] == "-":
                if map[current_row][current_col] == "O":
                    not_found_parts += 1
                current_row -= 1
                current_col -= 1

    if (target == "O" and not_found_parts == 1) or (target == "X" and not_found_parts == 0):
        return "Recovered"

    return "Found"

# print(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]))
# print(dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]))
# print(dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]))
# print(dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]))
# print(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]))
# print(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]))