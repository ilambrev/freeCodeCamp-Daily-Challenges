def game_of_life(grid):
    next_grid_state = [[0] * len(grid[0]) for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            live_neighbors = 0

            if i - 1 >= 0 and grid[i - 1][j] == 1:
                live_neighbors += 1
            
            if i - 1 >= 0 and j + 1 < len(grid[i]) and grid[i - 1][j + 1] == 1:
                live_neighbors += 1
            
            if j + 1 < len(grid[i]) and grid[i][j + 1] == 1:
                live_neighbors += 1
            
            if i + 1 < len(grid) and j + 1 < len(grid[i]) and grid[i + 1][j + 1] == 1:
                live_neighbors += 1
            
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                live_neighbors += 1
            
            if i + 1 < len(grid) and j - 1 >= 0 and grid[i + 1][j - 1] == 1:
                live_neighbors += 1
            
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                live_neighbors += 1
            
            if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] == 1:
                live_neighbors += 1
            
            if grid[i][j] == 1 and live_neighbors < 2 or live_neighbors > 3:
                next_grid_state[i][j] = 0
            elif grid[i][j] == 0 and live_neighbors == 3:
                next_grid_state[i][j] = 1
            else:
                next_grid_state[i][j] = grid[i][j]

    return next_grid_state

# print(game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]))
# print(game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]))
# print(game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
# print(game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]))