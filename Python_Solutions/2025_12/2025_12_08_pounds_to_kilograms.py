def convert_to_kgs(lbs):
    kgs = lbs * 0.453592

    lbs_num = "pounds"

    if lbs == 1:
        lbs_num = "pound"

    kgs_num = "kilograms"

    if f"{kgs:.2f}" == "1.00":
        kgs_num = "kilogram"

    return f"{lbs} {lbs_num} equals {kgs:.2f} {kgs_num}."

# print(convert_to_kgs(1))
# print(convert_to_kgs(0))
# print(convert_to_kgs(100))
# print(convert_to_kgs(2.5))
# print(convert_to_kgs(2.20462))