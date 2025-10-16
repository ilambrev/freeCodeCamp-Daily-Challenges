def mile_pace(miles, duration):
    total_minutes, total_seconds = duration.split(":")

    duration_in_seconds = int(total_minutes) * 60 + int(total_seconds)
    seconds_per_mile = duration_in_seconds / miles

    minutes_per_mile = int(seconds_per_mile / 60)
    seconds_per_mile = int(seconds_per_mile - minutes_per_mile * 60)

    return f"{minutes_per_mile:02}:{seconds_per_mile:02}"

# print(mile_pace(3, "24:00"))
# print(mile_pace(1, "06:45"))
# print(mile_pace(2, "07:00"))
# print(mile_pace(26.2, "120:35"))