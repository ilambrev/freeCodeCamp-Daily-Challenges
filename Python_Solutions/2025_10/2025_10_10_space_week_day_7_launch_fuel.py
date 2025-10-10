def launch_fuel(payload):
    total_fuel = payload / 5
    additional_payload = total_fuel

    while additional_payload >= 1:
        current_fuel_amount = additional_payload / 5
        total_fuel += current_fuel_amount
        additional_payload = current_fuel_amount

    return round(total_fuel, 1)

# print(launch_fuel(50))
# print(launch_fuel(500))
# print(launch_fuel(243))
# print(launch_fuel(11000))
# print(launch_fuel(6214))