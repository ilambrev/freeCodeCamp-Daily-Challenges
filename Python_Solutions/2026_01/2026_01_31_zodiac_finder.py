def get_sign(date_str):
    thresholds = {
        1: 20,
        2: 19,
        3: 21,
        4: 20,
        5: 21,
        6: 21,
        7: 23,
        8: 23,
        9: 23,
        10: 23,
        11: 22,
        12: 22
    }
    zodiac_signs = [
        "Aquarius",
        "Pisces",
        "Aries",
        "Taurus",
        "Gemini",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Scorpio",
        "Sagittarius",
        "Capricorn"
    ]

    year, month, day = date_str.split("-")

    if int(day) >= thresholds[int(month)]:
        return zodiac_signs[int(month) - 1]
    else:
        return zodiac_signs[int(month) - 2]

# print(get_sign("2026-01-31"))
# print(get_sign("2001-06-10"))
# print(get_sign("1985-09-07"))
# print(get_sign("2023-03-19"))
# print(get_sign("2045-11-05"))
# print(get_sign("1985-12-06"))
# print(get_sign("2025-12-30"))
# print(get_sign("2018-10-08"))
# print(get_sign("1958-05-04"))