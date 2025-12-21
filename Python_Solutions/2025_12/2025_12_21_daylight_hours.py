def daylight_hours(latitude):
    latitudes_hours = [[-90, 24], [-75, 23], [-60, 21], [-45, 15], [-30, 13], [-15, 12],
                       [0, 12], [15, 11], [30, 10], [45, 9], [60, 6], [75, 2], [90, 0]]

    latitudes = [l[0] for l in latitudes_hours]

    if latitude in latitudes:
        return latitudes_hours[latitudes.index(latitude)][1]

    min_difference = abs(latitude - latitudes_hours[0][0])
    index = 0

    for i in range(1, len(latitudes_hours)):
        current_difference = abs(latitude - latitudes_hours[i][0])

        if current_difference < min_difference:
            min_difference = current_difference
            index = i

    return latitudes_hours[index][1]

# print(daylight_hours(45))
# print(daylight_hours(0))
# print(daylight_hours(-90))
# print(daylight_hours(-10))
# print(daylight_hours(23))
# print(daylight_hours(88))
# print(daylight_hours(-33))
# print(daylight_hours(70))