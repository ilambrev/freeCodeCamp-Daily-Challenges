from math import ceil

def fuel_to_add(current_gallons, required_liters):
    GALON_TO_LITERS = 3.78541

    current_liters = current_gallons * GALON_TO_LITERS

    if current_liters >= required_liters:
        return 0

    return ceil((required_liters - current_liters) / GALON_TO_LITERS)

# print(fuel_to_add(0, 1))
# print(fuel_to_add(5, 40))
# print(fuel_to_add(10, 30))
# print(fuel_to_add(896, 20500))
# print(fuel_to_add(1000, 50000))