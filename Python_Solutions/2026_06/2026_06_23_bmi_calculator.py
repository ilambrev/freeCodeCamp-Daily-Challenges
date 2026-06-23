def calculate_bmi(weight, height):
    bmi = (weight / height ** 2) * 703

    return round(bmi, 1)

# print(calculate_bmi(180, 70))
# print(calculate_bmi(140, 64))
# print(calculate_bmi(160, 76))
# print(calculate_bmi(200, 60))
# print(calculate_bmi(150, 68))