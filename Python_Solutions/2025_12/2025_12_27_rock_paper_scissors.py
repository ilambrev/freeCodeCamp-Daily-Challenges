def rock_paper_scissors(player1, player2):
    if player1 == player2:
        return "Tie"

    options = {
        "RockScissors": "Player 1 wins",
        "PaperRock": "Player 1 wins",
        "ScissorsPaper": "Player 1 wins",
        "ScissorsRock": "Player 2 wins",
        "RockPaper": "Player 2 wins",
        "PaperScissors": "Player 2 wins"
    }

    return options[player1 + player2]

# print(rock_paper_scissors("Rock", "Rock"))
# print(rock_paper_scissors("Rock", "Paper"))
# print(rock_paper_scissors("Scissors", "Paper"))
# print(rock_paper_scissors("Rock", "Scissors"))
# print(rock_paper_scissors("Scissors", "Scissors"))
# print(rock_paper_scissors("Scissors", "Rock"))