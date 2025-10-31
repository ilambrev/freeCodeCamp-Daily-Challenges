def spookify(boo):
    is_previous_uppercase = False

    result = []

    for symbol in boo:
        if symbol == "_" or symbol == "-":
            result.append("~")
        else:
            if is_previous_uppercase:
                result.append(symbol.lower())
                is_previous_uppercase = False
            else:
                result.append(symbol.upper())
                is_previous_uppercase = True

    return "".join(result)

# print(spookify("hello_world"))
# print(spookify("Spooky_Case"))
# print(spookify("TRICK-or-TREAT"))
# print(spookify("c_a-n_d-y_-b-o_w_l"))
# print(spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts"))