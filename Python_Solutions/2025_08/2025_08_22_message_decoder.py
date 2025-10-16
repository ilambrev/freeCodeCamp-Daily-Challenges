from string import ascii_lowercase, ascii_uppercase

def decode(message, shift):
    symbols = [symbol for symbol in message]

    for i in range(len(symbols)):
        source = ""

        if symbols[i] in ascii_lowercase:
            source = ascii_lowercase
        elif symbols[i] in ascii_uppercase:
            source = ascii_uppercase
        else:
            continue

        index = source.find(symbols[i])
            
        if shift > 0:
            symbols[i] = source[index - shift if index - shift >= 0 else 26 - (shift - index)]
        else:
            symbols[i] = source[index - shift if index - shift < 26 else index - shift - 26]

    return ''.join(symbols)

# print(decode("Xlmw mw e wigvix qiwweki.", 4))
# print(decode("Byffi Qilfx!", 20))
# print(decode("Zqd xnt njzx?", -1))
# print(decode("oannLxmnLjvy", 9))