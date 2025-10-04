def classification(temp):
    classification = ''

    if 0 <= temp < 3_700:
        classification = "M"
    elif 3_700 <= temp < 5_200:
        classification = "K"
    elif 5_200 <= temp < 6_000:
        classification = "G"
    elif 6_000 <= temp < 7_500:
        classification = "F"
    elif 7_500 <= temp < 10_000:
        classification = "A"
    elif 10_000 <= temp < 30_000:
        classification = "B"
    elif temp >= 30_000:
        classification = "O"

    return classification

# print(classification(5778))
# print(classification(2400))
# print(classification(9999))
# print(classification(3700))
# print(classification(3699))
# print(classification(210000))
# print(classification(6000))
# print(classification(11432))