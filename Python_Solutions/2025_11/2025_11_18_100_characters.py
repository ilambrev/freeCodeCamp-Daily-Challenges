def one_hundred(chars):
    result = ""

    while len(result) < 100:
        result += chars

    return result[:100]

# print(one_hundred("One hundred "))
# print(one_hundred("freeCodeCamp "))
# print(one_hundred("daily challenges "))
# print(one_hundred("!"))