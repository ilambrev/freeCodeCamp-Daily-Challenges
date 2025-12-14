def title_case(title):
    words = [word.capitalize() for word in title.split()]

    return " ".join(words)

# print(title_case("hello world"))
# print(title_case("the quick brown fox"))
# print(title_case("JAVASCRIPT AND PYTHON"))
# print(title_case("AvOcAdO tOAst fOr brEAkfAst"))