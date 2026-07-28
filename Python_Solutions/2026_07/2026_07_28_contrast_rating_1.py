def get_contrast_rating(ratio, is_large_text):
    ratio_as_number = float(ratio)

    if is_large_text:
        if ratio_as_number >= 4.5 and ratio_as_number < 7.0:
            return "AAA"
        elif ratio_as_number >= 3.0 and ratio_as_number < 4.5:
            return "AA"
        elif ratio_as_number < 3.0:
            return "Fail"
    else:
        if ratio_as_number >= 7.0:
            return "AAA"
        elif ratio_as_number >= 4.5 and ratio_as_number < 7.0:
            return "AA"
        elif ratio_as_number < 4.5:
            return "Fail"

# print(get_contrast_rating("7.5", False))
# print(get_contrast_rating("4.8", False))
# print(get_contrast_rating("4.2", False))
# print(get_contrast_rating("4.5", True))
# print(get_contrast_rating("3.0", True))
# print(get_contrast_rating("2.7", False))