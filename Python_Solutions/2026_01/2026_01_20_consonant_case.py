from string import ascii_letters

def to_consonant_case(s):
    symbols = [symbol for symbol in s]
    vowels = "aeiou"

    for i in range(len(symbols)):
        current_symbol = symbols[i]
        if current_symbol.lower() in vowels:
            symbols[i] = current_symbol.lower()
        elif current_symbol in ascii_letters:
            symbols[i] = current_symbol.upper()
        elif current_symbol == "-":
            symbols[i] = "_"

    return "".join(symbols)

# print(to_consonant_case("helloworld"))
# print(to_consonant_case("HELLOWORLD"))
# print(to_consonant_case("_hElLO-WOrlD-"))
# print(to_consonant_case("_~-generic_~-variable_~-name_~-here-~_"))