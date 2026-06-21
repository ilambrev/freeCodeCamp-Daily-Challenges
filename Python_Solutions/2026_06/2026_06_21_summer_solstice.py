def get_daytime_hours(latitude):
    daytime_hours = int(12 + (latitude / 90) * 12)

    if not daytime_hours % 2 == 0:
        daytime_hours += 1
    
    nighttime_hours_half = int((24 - daytime_hours) / 2)
    
    return f"{'🌑' * nighttime_hours_half}{'☀️' * daytime_hours}{'🌑' * nighttime_hours_half}"

# print(get_daytime_hours(0))
# print(get_daytime_hours(90))
# print(get_daytime_hours(-90))
# print(get_daytime_hours(-33))
# print(get_daytime_hours(66.5))
# print(get_daytime_hours(40))
# print(get_daytime_hours(-50))