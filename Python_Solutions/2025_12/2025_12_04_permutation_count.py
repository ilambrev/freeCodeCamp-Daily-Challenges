from math import factorial as f

def count_permutations(s):
    letters = {}

    for letter in s:
        if not letter in letters:
            letters[letter] = 0

        letters[letter] += 1

    numerator = f(len(s))
    denominator = 1

    for v in letters.values():
        denominator *= f(v)

    return int(numerator / denominator)

# print(count_permutations("abb"))
# print(count_permutations("abc"))
# print(count_permutations("racecar"))
# print(count_permutations("freecodecamp"))