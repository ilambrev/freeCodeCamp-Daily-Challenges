def get_fastest_speed(times):
    segments_distances = {
        1: 320,
        2: 280,
        3: 350,
        4: 300,
        5: 250
    }

    speeds = [segments_distances[i + 1] / times[i] for i in range(len(times))]
    max_speed = max(speeds)
    segment_with_max_speed = speeds.index(max_speed) + 1

    return f"The luger's fastest speed was {max_speed:.2f} m/s on segment {segment_with_max_speed}."

# print(get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]))
# print(get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284]))
# print(get_fastest_speed([8.890, 7.601, 9.093, 8.392, 6.912]))
# print(get_fastest_speed([8.490, 7.732, 10.103, 8.489, 6.840]))
# print(get_fastest_speed([8.204, 7.230, 9.673, 7.645, 6.508]))