def find_coorinates(matrix, turn):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == turn:
                return [i, j]

def get_next_location(matrix):
    previous_ball_location = find_coorinates(matrix, 1)
    ball_location = find_coorinates(matrix, 2)

    direction = [ball_location[0] - previous_ball_location[0], ball_location[1] - previous_ball_location[1]]

    new_ball_location = [ball_location[0], ball_location[1]]

    if new_ball_location[0] + direction[0] >= 0 and new_ball_location[0] + direction[0] < len(matrix):
        new_ball_location[0] += direction[0]
    else:
        new_ball_location[0] -= direction[0]
    
    if new_ball_location[1] + direction[1] >= 0 and new_ball_location[1] + direction[1] < len(matrix[0]):
        new_ball_location[1] += direction[1]
    else:
        new_ball_location[1] -= direction[1]

    return new_ball_location

# print(get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]))
# print(get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]))
# print(get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]))
# print(get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]))
# print(get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]))