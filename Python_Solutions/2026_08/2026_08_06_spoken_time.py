def get_spoken_time(hour_angle, minute_angle):
    minute_to_degrees = 360 / 60
    hour_to_degrees = 360 / 12
    minutes = int(minute_angle / minute_to_degrees)
    hours = round(hour_angle / hour_to_degrees)

    spoken_time = ""

    if minutes == 0:
        spoken_time = f"{hours} o'clock"
    elif minutes == 15:
        spoken_time = f"quarter past {hours}"
    elif (minutes > 0 and minutes < 15) or (minutes > 15 and minutes < 30):
        spoken_time = f"{minutes} minutes past {hours}"
    elif minutes == 30:
        spoken_time = f"half past {hours}"
    elif minutes == 45:
        spoken_time = f"quarter to {hours}"
    elif (minutes > 30 and minutes < 45) or (minutes > 45 and minutes < 59):
        spoken_time = f"{60 - minutes} minutes to {hours}"

    return spoken_time

# print(get_spoken_time(90, 0))
# print(get_spoken_time(160, 120))
# print(get_spoken_time(255, 180))
# print(get_spoken_time(67.5, 92))
# print(get_spoken_time(200, 240))
# print(get_spoken_time(322.5, 273))
# print(get_spoken_time(117.5, 335))