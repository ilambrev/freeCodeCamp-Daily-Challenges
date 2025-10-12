from string import ascii_letters

def battle(our_team, opponent):
    our_team_words = our_team.split()
    opponent_words = opponent.split()

    our_wins = 0
    opponent_wins = 0

    def calculate_letter_value(letter):
        letter_value = ascii_letters.index(letter) + 1

        return letter_value if letter_value < 27 else (letter_value - 26) * 2

    for i in range(len(our_team_words)):
        our_word_value = sum([calculate_letter_value(letter) for letter in our_team_words[i]])
        opponent_word_value = sum([calculate_letter_value(letter) for letter in opponent_words[i]])

        if our_word_value > opponent_word_value:
            our_wins += 1
        elif opponent_word_value > our_word_value:
            opponent_wins += 1

    result = "Draw"

    if our_wins > opponent_wins:
        result = "We win"
    elif opponent_wins > our_wins:
        result = "We lose"
    
    return result

# print(battle("hello world", "hello word"))
# print(battle("Hello world", "hello world"))
# print(battle("lorem ipsum", "kitty ipsum"))
# print(battle("hello world", "world hello"))
# print(battle("git checkout", "git switch"))
# print(battle("Cheeseburger with fries", "Cheeseburger with Fries"))
# print(battle("We must never surrender", "Our team must win"))