def get_shadow(time):
    rise = 6
    noon = 12
    set = 18
    hours, minutes = (int(t) for t in time.split(":"))
    hours += 0 if minutes == 0 else 0.5
    difference = noon - hours

    if difference == 0 or difference > 6 or difference <= -6:
        return "No shadow"

    feets = abs(difference) ** 3
    direction = "east" if difference < 0 else "west"

    return f"{feets}ft {direction}"

# print(get_shadow("10:00"))  # should return "8ft west"
# print(get_shadow("15:00"))  # should return "27ft east"
# print(get_shadow("12:00"))  # should return "No shadow"
# print(get_shadow("17:30"))  # should return "166.375ft east"
# print(get_shadow("05:00"))  # should return "No shadow"
# print(get_shadow("06:00"))  # should return "216ft west"
# print(get_shadow("18:00"))  # should return "No shadow"
# print(get_shadow("07:30"))  # should return "91.125ft west"
# print(get_shadow("00:00"))  # should return "No shadow"