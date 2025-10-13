def speeding(speeds, limit):
    speeding_vehicles = 0
    average_speed_beyond_limit = 0.0

    for speed in speeds:
        if speed > limit:
            speeding_vehicles += 1
            average_speed_beyond_limit += speed - limit

    if speeding_vehicles > 0:
        average_speed_beyond_limit /= speeding_vehicles

    if average_speed_beyond_limit.is_integer():
        average_speed_beyond_limit = int(average_speed_beyond_limit)

    return [speeding_vehicles, average_speed_beyond_limit]

# print(speeding([50, 60, 55], 60))
# print(speeding([58, 50, 60, 55], 55))
# print(speeding([61, 81, 74, 88, 65, 71, 68], 70))
# print(speeding([100, 105, 95, 102], 100))
# print(speeding([40, 45, 44, 50, 112, 39], 55))