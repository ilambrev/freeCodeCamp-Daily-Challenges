def count_letters_and_numbers(s):
    letters_count = sum(1 for char in s if char.isalpha())
    numbers_count = sum(1 for char in s if char.isdigit())

    plural = lambda count, word: f"{count} {word}{'' if count == 1 else 's'}"

    return f"The string has {plural(letters_count, 'letter')} and {plural(numbers_count, 'number')}."

# print(count_letters_and_numbers("helloworld123"))
# print(count_letters_and_numbers("Catch 22"))
# print(count_letters_and_numbers("A1!"))
# print(count_letters_and_numbers("12345"))
# print(count_letters_and_numbers("password"))