def get_contrast_rating(rgb1, rgb2, is_large_text):

    def convert_rgb_to_luminance(rgb):
        relative_luminances = [c / 255 for c in rgb]
        for i in range(len(relative_luminances)):
            if relative_luminances[i] <= 0.04045:
                relative_luminances[i] /= 12.92
            else:
                relative_luminances[i] = ((relative_luminances[i] + 0.055) / 1.055) ** 2.4

        return 0.2126 * relative_luminances[0] + 0.7152 * relative_luminances[1] + 0.0722 * relative_luminances[2]

    l1 = convert_rgb_to_luminance(rgb1)
    l2 = convert_rgb_to_luminance(rgb2)

    ratio = (l1 + 0.05) / (l2 + 0.05)

    if is_large_text:
        if ratio >= 4.5:
            return "AAA"
        elif ratio >= 3.0:
            return "AA"
        elif ratio < 3.0:
            return "Fail"
    else:
        if ratio >= 7.0:
            return "AAA"
        elif ratio >= 4.5:
            return "AA"
        elif ratio < 4.5:
            return "Fail"

# print(get_contrast_rating([255, 255, 255], [0, 0, 0], False))
# print(get_contrast_rating([215, 188, 188], [55, 55, 55], False))
# print(get_contrast_rating([143, 144, 210], [46, 47, 61], False))
# print(get_contrast_rating([167, 167, 210], [53, 10, 53], True))
# print(get_contrast_rating([135, 147, 155], [60, 70, 90], True))
# print(get_contrast_rating([125, 210, 195], [105, 130, 90], True))