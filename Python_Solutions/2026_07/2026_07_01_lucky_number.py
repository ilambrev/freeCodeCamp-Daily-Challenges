def get_lucky_number(name):
    vowels = "aeiouy"
    first_name, last_name = name.split()
    vowel_first_name_count = len(
        [l for l in first_name if l.lower() in vowels])
    consonant_first_name_count = len(first_name) - vowel_first_name_count
    vowel_last_name_count = len([l for l in last_name if l.lower() in vowels])
    consonant_last_name_count = len(last_name) - vowel_last_name_count
    smaller_points = min(vowel_first_name_count, vowel_last_name_count) * min(
        consonant_first_name_count, consonant_last_name_count) * min(len(first_name), len(last_name))
    larger_points = max(vowel_first_name_count, vowel_last_name_count) * max(
        consonant_first_name_count, consonant_last_name_count) * max(len(first_name), len(last_name))

    diff = larger_points - smaller_points

    return 13 if diff == 0 else diff

# print(get_lucky_number("John Doe"))
# print(get_lucky_number("Olivia Lewis"))
# print(get_lucky_number("James Wilson"))
# print(get_lucky_number("Elizabeth Hernandez"))
# print(get_lucky_number("Mike Walker"))
# print(get_lucky_number("Chloe Perez"))