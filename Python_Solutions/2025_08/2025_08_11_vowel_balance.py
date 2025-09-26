def is_balanced(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    first_half_count = len([v for v in s[:int(len(s) / 2)] if v.lower() in vowels])
    second_half_count = len([v for v in s[
        int(len(s) / 2) if len(s) % 2 == 0 else int(len(s) / 2) + 1:] if v.lower() in vowels])

    return first_half_count == second_half_count

# print(is_balanced("racecar"))
# print(is_balanced("Lorem Ipsum"))
# print(is_balanced("Kitty Ipsum"))
# print(is_balanced("string"))
# print(is_balanced(" "))
# print(is_balanced("abcdefghijklmnopqrstuvwxyz"))
# print(is_balanced("123A#b!E&*456-o.U"))