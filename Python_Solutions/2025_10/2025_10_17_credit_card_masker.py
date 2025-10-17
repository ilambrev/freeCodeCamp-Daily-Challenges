from string import digits

def mask(card):
    masked_version = []

    for i in range(len(card)):
        current_symbol = card[i]

        if current_symbol in digits and i < len(card) - 4:
            current_symbol = "*"

        masked_version.append(current_symbol)

    return "".join(masked_version)

# print(mask("4012-8888-8888-1881"))
# print(mask("5105 1051 0510 5100"))
# print(mask("6011 1111 1111 1117"))
# print(mask("2223-0000-4845-0010"))