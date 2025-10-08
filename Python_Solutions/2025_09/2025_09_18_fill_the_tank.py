def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    needed_fuel = tank_size - fuel_level
    total_cost = needed_fuel * price_per_gallon

    return f'${total_cost:.2f}'

# print(cost_to_fill(20, 0, 4.00))
# print(cost_to_fill(15, 10, 3.50))
# print(cost_to_fill(18, 9, 3.25))
# print(cost_to_fill(12, 12, 4.99))
# print(cost_to_fill(15, 9.5, 3.98))