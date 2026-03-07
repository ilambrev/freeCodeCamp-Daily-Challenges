def find_point_coordinates(map, point_sign):
    coordinates = [-1, -1]
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == point_sign:
                coordinates[0] = i
                coordinates[1] = j
                return coordinates

    return coordinates

def navigate_trail(map):
    current_location = "C"
    goal = "G"
    traversable_part = "T"
    untraversable_part = "-"
    ways = [[0, 1, "R"], [1, 0, "D"], [0, -1, "L"], [-1, 0, "U"]]

    row, col = find_point_coordinates(map, current_location)
    
    current_way_index = 0
    is_goal_reached = False
    moves = []

    while not is_goal_reached:
        for i in range(4):
            index = (current_way_index + i) % 4
            way = ways[index]
            
            if not way[0] == 0 and -way[0] == ways[current_way_index][0] or not way[1] == 0 and -way[1] == ways[current_way_index][1]:
                continue

            is_row_in_map = row + way[0] >= 0 and row + way[0] < len(map)
            is_col_in_map = col + way[1] >= 0 and col + way[1] < len(map[0])
            
            if is_row_in_map and is_col_in_map and map[row + way[0]][col + way[1]] == goal:
                moves.append(way[2])
                is_goal_reached = True
                break
            
            if is_row_in_map and is_col_in_map and map[row + way[0]][col + way[1]] == traversable_part:
                row = row + way[0]
                col = col + way[1]
                current_way_index = (current_way_index + i) % 4
                moves.append(way[2])
                break

    return "".join(moves)

# print(navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]))
# print(navigate_trail(["-----", "--TTG", "--T--", "--T--", "CTT--"]))
# print(navigate_trail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"]))
# print(navigate_trail(["--------", "-CTTT---", "----T---", "---GT---", "--------"]))
# print(navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"]))