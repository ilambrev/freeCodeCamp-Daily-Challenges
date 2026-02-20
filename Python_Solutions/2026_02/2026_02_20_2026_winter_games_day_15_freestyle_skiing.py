def is_valid_trick(trick_name):
    valid_first_words = ["Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"]
    valid_second_words = ["Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard", "Shadow"]
    first_word, second_word = trick_name.split()

    return first_word in valid_first_words and second_word in valid_second_words

# print(is_valid_trick("Polar Vortex"))
# print(is_valid_trick("Solar Icequake"))
# print(is_valid_trick("Thunder Blizzard"))
# print(is_valid_trick("Phantom Frostbite"))
# print(is_valid_trick("Ghost Avalanche"))
# print(is_valid_trick("Snowstorm Shadow"))
# print(is_valid_trick("Solar Sky"))