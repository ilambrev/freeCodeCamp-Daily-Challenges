from string import ascii_letters

def calculate_symbols_value(symbols):
    value = 0

    for symbol in symbols:
        if symbol in ascii_letters:
            value += ascii_letters.index(symbol) + 1
    
    return value

def verify(message, key, signature):
    text_value = calculate_symbols_value(message)
    key_value = calculate_symbols_value(key)

    return text_value + key_value == signature

# print(verify("foo", "bar", 57))
# print(verify("foo", "bar", 54))
# print(verify("freeCodeCamp", "Rocks", 238))
# print(verify("Is this valid?", "No", 210))
# print(verify("Is this valid?", "Yes", 233))
# print(verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514))