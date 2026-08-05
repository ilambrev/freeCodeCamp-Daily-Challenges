def get_spoken_duration(seconds):
    hours = int(seconds / 3600)
    minutes = int((seconds - hours * 3600) / 60)
    seconds -= hours * 3600 + minutes * 60

    strings = ["", "", ""]

    if hours > 0:
        strings[0] = f"{hours} hour{'' if hours == 1 else 's'}"

    if minutes > 0:
        strings[1] = f"{minutes} minute{'' if minutes == 1 else 's'}"

    if seconds > 0:
        strings[2] = f"{seconds} second{'' if seconds == 1 else 's'}"

    strings = [s for s in strings if s]
    non_empty_strings_count = len(strings)

    if non_empty_strings_count == 3:
        return f"{strings[0]}, {strings[1]} and {strings[2]}"
    elif non_empty_strings_count == 2:
        return f"{strings[0]} and {strings[1]}"
    elif non_empty_strings_count == 1:
        return f"{strings[0]}"
    else:
        return ""

# print(get_spoken_duration(3723))
# print(get_spoken_duration(7295))
# print(get_spoken_duration(8521))
# print(get_spoken_duration(435))
# print(get_spoken_duration(14455))
# print(get_spoken_duration(72000))
# print(get_spoken_duration(1))