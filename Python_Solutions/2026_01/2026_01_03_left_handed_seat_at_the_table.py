def find_left_handed_seats(table):
    available_sites = 0

    for i in range(len(table[0]) - 1):
        if table[0][i] == "U" and not table[0][i + 1] == "R":
            available_sites += 1

        if i == len(table[0]) - 2 and table[0][i + 1] == "U":
            available_sites += 1
    
    for i in range(1, len(table[1])):
        if table[1][i] == "U" and not table[1][i - 1] == "R":
            available_sites += 1

        if i == len(table[1]) - 1 and table[1][0] == "U":
            available_sites += 1

    return available_sites

# print(find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]))
# print(find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]]))
# print(find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]]))
# print(find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]]))
# print(find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]]))