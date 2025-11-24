def is_valid_message(message, validation):
    words = message.split()

    if not len(words) == len(validation):
        return False

    isValid = True

    for i in range(len(words)):
        if not words[i].lower().startswith(validation[i].lower()):
            isValid = False
            break

    return isValid

# print(is_valid_message("hello world", "hw"))
# print(is_valid_message("ALL CAPITAL LETTERS", "acl"))
# print(is_valid_message("Coding challenge are boring.", "cca"))
# print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"))
# print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"))