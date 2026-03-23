def has_no_repeats(s):
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return False

    return True

# print(has_no_repeats("hi world"))
# print(has_no_repeats("hello world"))
# print(has_no_repeats("abcdefghijklmnopqrstuvwxyz"))
# print(has_no_repeats("freeCodeCamp"))
# print(has_no_repeats("The quick brown fox jumped over the lazy dog."))
# print(has_no_repeats("Mississippi"))