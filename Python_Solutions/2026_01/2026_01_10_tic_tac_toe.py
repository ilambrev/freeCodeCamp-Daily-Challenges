def tic_tac_toe(board):
    def is_winner(board, player):
        win_pattern = player * 3

        for i in range(len(board)):
            if "".join(board[i]) == win_pattern:
                return True
        
        for j in range(len(board[0])):
            col = []
            
            for i in range(len(board)):
                col.append(board[i][j])
            
            if "".join(col) == win_pattern:
                return True

        if board[0][0] + board[1][1] + board[2][2] == win_pattern:
            return True
        
        if board[0][2] + board[1][1] + board[2][0] == win_pattern:
            return True

        return False
    
    o_result = is_winner(board, "O")
    x_result = is_winner(board, "X")

    if o_result:
        return "O wins"
    elif x_result:
        return "X wins"
    else:
        return "Draw"

# print(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]))
# print(tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "X", "X"]]))
# print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]))
# print(tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]))
# print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]))
# print(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]))