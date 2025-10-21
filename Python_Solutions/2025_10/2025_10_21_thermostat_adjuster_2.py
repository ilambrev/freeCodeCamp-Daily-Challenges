def adjust_thermostat(current_f, target_c):
    target_f = target_c * 1.8 + 32
    difference = target_f - current_f

    if difference > 0:
        return f"Heat: {difference:.1f} degrees Fahrenheit"
    elif difference < 0:
        return f"Cool: {-difference:.1f} degrees Fahrenheit"
    else:
        return "Hold"

# print(adjust_thermostat(32, 0))
# print(adjust_thermostat(70, 25))
# print(adjust_thermostat(72, 18))
# print(adjust_thermostat(212, 100))
# print(adjust_thermostat(59, 22))