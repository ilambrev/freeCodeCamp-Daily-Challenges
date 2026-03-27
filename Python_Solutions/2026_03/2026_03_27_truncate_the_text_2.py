def truncate_text(s):
    letters = {
        "ilI.": 1,
        "fjrt ": 2,
        "abcdeghkmnopqrstuvwxyzJL": 3,
        "ABCDEFGHKMNOPQRSTUVWXYZ": 4,
    }
    max_units = 50
    current_units = 0
    index = len(s) - 1

    def get_letter_value(letters, letter):
        for k, v in letters.items():
            if letter in k:
                return v

    for i in range(len(s)):
        letter = s[i]
        current_units += get_letter_value(letters, letter)

    if current_units <= max_units:
        return s

    while current_units > max_units - 3:
        letter = s[index]
        current_units -= get_letter_value(letters, letter)
        index -= 1

    return f"{s[:index+1]}..."

# print(truncate_text("The quick brown fox"))
# print(truncate_text("The silky smooth sloth"))
# print(truncate_text("THE LOUD BRIGHT BIRD"))
# print(truncate_text("The fast striped zebra"))
# print(truncate_text("The big black bear"))