def is_match(fingerprint_a, fingerprint_b):
    different_characters_percentage = 10

    if not len(fingerprint_a) == len(fingerprint_b):
        return False

    different_symbols = 0

    for i in range(len(fingerprint_a)):
        if not fingerprint_a[i] == fingerprint_b[i]:
            different_symbols += 1

    return not (different_symbols / len(fingerprint_a)) * 100 > different_characters_percentage

# print(is_match("helloworld", "helloworld"))
# print(is_match("helloworld", "helloworlds"))
# print(is_match("helloworld", "jelloworld"))
# print(is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog"))
# print(is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog"))
# print(is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat"))