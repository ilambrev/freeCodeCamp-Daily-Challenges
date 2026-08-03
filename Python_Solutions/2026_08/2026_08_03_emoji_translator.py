def get_emoji_phrase(s):
    emoji_phrases = {
        "👶": "baby",
        "🐱": "cat",
        "🐕": "dog",
        "🐟": "fish",
        "🥵": "hot",
        "🧊": "ice",
        "🪨": "rock",
        "🦈": "shark",
        "🍲": "soup",
        "⭐": "star"
    }

    return " ".join([emoji_phrases.get(e, "") for e in s])

# print(get_emoji_phrase("🪨⭐"))
# print(get_emoji_phrase("🥵🐕"))
# print(get_emoji_phrase("👶🦈"))
# print(get_emoji_phrase("⭐🐟"))
# print(get_emoji_phrase("🧊🧊👶"))
# print(get_emoji_phrase("🐱🐟🍲"))