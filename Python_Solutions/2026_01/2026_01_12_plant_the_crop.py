def get_number_of_plants(field_size, unit, crop):
    crops = {
        "corn": 1,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2
    }
    field_sq_metters = 0

    if unit == "acres":
        field_sq_metters = field_size * 4046.86
    elif unit == "hectares":
        field_sq_metters = field_size * 10000

    if crop in crops:
        return int(field_sq_metters / crops[crop])
    else:
        return 0

# print(get_number_of_plants(1, "acres", "corn"))
# print(get_number_of_plants(2, "hectares", "lettuce"))
# print(get_number_of_plants(20, "acres", "soybeans"))
# print(get_number_of_plants(3.75, "hectares", "tomatoes"))
# print(get_number_of_plants(16.75, "acres", "tomatoes"))