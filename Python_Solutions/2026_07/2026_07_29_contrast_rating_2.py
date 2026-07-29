def get_contrast_rating(l1, l2, is_large_text):
    ratio = (l1 + 0.05) / (l2 + 0.05)

    if is_large_text:
        if ratio >= 4.5 and ratio < 7.0:
            return "AAA"
        elif ratio >= 3.0 and ratio < 4.5:
            return "AA"
        elif ratio < 3.0:
            return "Fail"
    else:
        if ratio >= 7.0:
            return "AAA"
        elif ratio >= 4.5 and ratio < 7.0:
            return "AA"
        elif ratio < 4.5:
            return "Fail"

# print(get_contrast_rating(1.0, 0.0, False))
# print(get_contrast_rating(0.9015, 0.1364, False))
# print(get_contrast_rating(0.8965, 0.1628, False))
# print(get_contrast_rating(0.7469, 0.0957, True))
# print(get_contrast_rating(0.7489, 0.2018, True))
# print(get_contrast_rating(0.6571, 0.1974, True))