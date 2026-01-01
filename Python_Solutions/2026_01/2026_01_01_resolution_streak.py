def resolution_streak(days):
    steps = 10000
    screen_time = 120
    pages = 5

    streak = 0

    for i in range(len(days)):
        if days[i][0] >= steps and days[i][1] <= screen_time and days[i][2] >= 5:
            streak += 1
        else:
            return f"Resolution failed on day {i + 1}: {streak} day streak."

    return f"Resolution on track: {streak} day streak."

# print(resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]]))
# print(resolution_streak([[10000, 120, 5], [10950, 121, 11]]))
# print(resolution_streak([[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]]))
# print(resolution_streak([[11600, 76, 13], [12556, 64, 26], [10404, 32, 59], [9999, 44, 124], [7508, 23, 167], [10900, 80, 0]]))
# print(resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9], [10200, 60, 10], [10678, 87, 9], [12431, 67, 13], [10444, 107, 19], [10111, 95, 5], [10000, 120, 7], [11980, 101, 8]]))