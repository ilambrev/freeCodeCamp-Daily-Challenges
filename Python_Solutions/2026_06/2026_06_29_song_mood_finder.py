def get_mood(genre, bpm):
    genres = {
        "electronic": [[60, 89, "focus"], [90, 134, "happy"], [135, 180, "hype"]],
        "rock": [[60, 129, "happy"], [130, 180, "hype"]],
        "classical": [[60, 109, "focus"], [110, 180, "happy"]],
        "pop": [[60, 180, "happy"]]
    }

    mood = ""

    if genre in genres:
        genre_options = genres[genre]
        for option in genre_options:
            if bpm >= option[0] and bpm <= option[1]:
                mood = option[2]

    return mood

# print(get_mood("rock", 111))
# print(get_mood("electronic", 74))
# print(get_mood("classical", 180))
# print(get_mood("rock", 155))
# print(get_mood("electronic", 90))
# print(get_mood("classical", 67))
# print(get_mood("pop", 100))
# print(get_mood("electronic", 135))