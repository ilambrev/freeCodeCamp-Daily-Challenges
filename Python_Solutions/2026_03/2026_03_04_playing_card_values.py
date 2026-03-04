def card_values(cards):
    cards_values = {
        "A": 1,
        "K": 10,
        "Q": 10,
        "J": 10,
        "10": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }

    return [cards_values[card[:-1]] for card in cards]

# print(card_values(["3H", "4D", "5S"]))
# print(card_values(["AS", "10S", "10H", "6D", "7D"]))
# print(card_values(["8D", "QS", "2H", "JC", "9C"]))
# print(card_values(["AS", "KS"]))
# print(card_values(["10H", "JH", "QH", "KH", "AH"]))