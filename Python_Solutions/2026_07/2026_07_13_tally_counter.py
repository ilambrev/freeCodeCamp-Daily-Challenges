def get_tally_count(s):
    groups = s.split()
    tally_counter = (len(groups) - 1) * 5
    tally_counter += groups[-1].count("|") if len(groups[-1]) < 5 else 5

    return tally_counter

# print(get_tally_count("||||"))
# print(get_tally_count("||||/"))
# print(get_tally_count("||||/ |||"))
# print(get_tally_count("||||/ ||||/ ||||/ ||"))
# print(get_tally_count("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |"))