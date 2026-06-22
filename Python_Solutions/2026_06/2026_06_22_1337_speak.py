def make_leet(s):
    letters = {
        "a": "4",
        "e": "3",
        "g": "9",
        "i": "1",
        "l": "1",
        "o": "0",
        "s": "5",
        "t": "7"
    }

    return "".join([l if not l in letters else letters[l] for l in s])

# print(make_leet("cool"))
# print(make_leet("leet"))
# print(make_leet("hacker"))
# print(make_leet("satellite"))
# print(make_leet("abcdefghijklmnopqrstuvwxyz"))