from math import factorial

def combinations(cards):
    cards_in_deck = 52

    return int((factorial(cards_in_deck) / ((factorial(cards)) * factorial(cards_in_deck - cards))))

# print(combinations(52))
# print(combinations(1))
# print(combinations(2))
# print(combinations(5))
# print(combinations(10))
# print(combinations(50))