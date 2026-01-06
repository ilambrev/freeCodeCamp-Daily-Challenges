def vowel_case(s):
    vowels = "aeiou"

    return "".join([symbol.upper() if symbol in vowels else symbol for symbol in s.lower()])

# print(vowel_case("vowelcase"))
# print(vowel_case("coding is fun"))
# print(vowel_case("HELLO, world!"))
# print(vowel_case("git cherry-pick"))
# print(vowel_case("HEAD~1"))