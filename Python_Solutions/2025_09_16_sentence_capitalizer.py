def capitalize(paragraph):
    sentence_end_symbols = ['.', '?', '!']
    symbols = [symbol for symbol in paragraph]

    if symbols:
        symbols[0] = symbols[0].upper()

    is_end_symbol = False

    for i in range(len(symbols)):
        if symbols[i] in sentence_end_symbols:
            is_end_symbol = True
        elif not symbols[i] == ' ' and is_end_symbol:
            symbols[i] = symbols[i].upper()
            is_end_symbol = False

    return ''.join(symbols)

# print(capitalize("this is a simple sentence."))
# print(capitalize("hello world. how are you?"))
# print(capitalize("i did today's coding challenge... it was fun!!"))
# print(capitalize("crazy!!!strange???unconventional...sentences."))
# print(capitalize("there's a space before this period . why is there a space before that period ?"))