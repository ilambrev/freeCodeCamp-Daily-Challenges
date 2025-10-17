from string import digits, ascii_letters

def battle(my_army, opposing_army):
    my_wins = 0
    opposing_wins = 0

    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(my_army) < len(opposing_army):
        return "We retreated"

    for i in range(len(my_army)):
        my_strength = 0
        opposing_strength = 0

        if my_army[i] in digits:
            my_strength = int(my_army[i])
        elif my_army[i] in ascii_letters:
            my_strength = ascii_letters.find(my_army[i]) + 1

        if opposing_army[i] in digits:
            opposing_strength = int(opposing_army[i])
        elif opposing_army[i] in ascii_letters:
            opposing_strength = ascii_letters.find(opposing_army[i]) + 1

        if my_strength > opposing_strength:
            my_wins += 1
        elif my_strength < opposing_strength:
            opposing_wins += 1

    result = "It was a tie"

    if my_wins > opposing_wins:
        result = "We won"
    elif my_wins < opposing_wins:
        result = "We lost"

    return result

# print(battle("Hello", "World"))
# print(battle("pizza", "salad"))
# print(battle("C@T5", "D0G$"))
# print(battle("kn!ght", "orc"))
# print(battle("PC", "Mac"))
# print(battle("Wizards", "Dragons"))
# print(battle("Mr. Smith", "Dr. Jones"))