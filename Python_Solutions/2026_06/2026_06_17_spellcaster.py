def cast(spells):
    names = {
        "f": ["Destruction", 3],
        "l": ["Destruction", 3],
        "i": ["Control", 2],
        "w": ["Control", 2],
        "h": ["Restoration", 1],
        "s": ["Restoration", 1]
    }

    multiplayer = 0
    total_score = 0
    current_cathegory = ""

    for spell in spells:
        cathegory, score = names[spell]

        if not current_cathegory or cathegory == current_cathegory:
            multiplayer = 1
        else:
            multiplayer += 1

        total_score += multiplayer * score

        current_cathegory = cathegory

    return total_score

# print(cast("fihwl"))
# print(cast("lwswfi"))
# print(cast("wislhfl"))
# print(cast("sihwlih"))
# print(cast("wishlfihwslwifihl"))