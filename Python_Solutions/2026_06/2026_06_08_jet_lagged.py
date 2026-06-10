def get_jet_lag_hours(departure_city, arrival_city, flight_duration, direction):
    directions = {
        "Los Angeles": -8,
        "New York": -5,
        "London": 0,
        "Istanbul": 3,
        "Dubai": 4,
        "Hong Kong": 8,
        "Tokyo": 9
    }

    departure_city_utc_offset = directions[departure_city]
    arrival_city_utc_offset = directions[arrival_city]
    timezone_difference = abs(departure_city_utc_offset - arrival_city_utc_offset)
    direction_multiplier = 1.5 if direction == "east" else 1.0

    jet_lag = timezone_difference + (flight_duration * 0.1) * direction_multiplier

    return round(jet_lag, 1)

# print(get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east"))
# print(get_jet_lag_hours("London", "New York", 8, "west"))
# print(get_jet_lag_hours("Hong Kong", "Tokyo", 4, "east"))
# print(get_jet_lag_hours("Dubai", "London", 7, "west"))
# print(get_jet_lag_hours("Los Angeles", "Hong Kong", 15, "west"))
# print(get_jet_lag_hours("Tokyo", "Dubai", 9, "west"))
# print(get_jet_lag_hours("New York", "Istanbul", 10, "east"))