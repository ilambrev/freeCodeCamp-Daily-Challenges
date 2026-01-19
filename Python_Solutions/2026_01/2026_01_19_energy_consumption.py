def compare_energy(calories_burned, watt_hours_used):
    calorie_to_joules = 4184
    watt_hour_to_joules = 3600

    workout_joules = calories_burned * calorie_to_joules
    devices_joules = watt_hours_used * watt_hour_to_joules

    if workout_joules > devices_joules:
        return "Workout"
    elif workout_joules < devices_joules:
        return "Devices"
    else:
        return "Equal"

# print(compare_energy(250, 50))
# print(compare_energy(100, 200))
# print(compare_energy(450, 523))
# print(compare_energy(300, 75))
# print(compare_energy(200, 250))
# print(compare_energy(900, 1046))