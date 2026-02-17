def check_eligibility(athlete_weights, sled_weight):
    bobsled_weight = {
        1: [162, 247],
        2: [170, 390],
        4: [210, 630]
    }

    team_size = len(athlete_weights)
    bobsled_total_weight = sum(athlete_weights) + sled_weight

    return ("Eligible" if bobsled_weight[team_size][0] <= sled_weight and
            bobsled_total_weight <= bobsled_weight[team_size][1] else "Not Eligible")

# print(check_eligibility([78], 165))
# print(check_eligibility([80], 160))
# print(check_eligibility([80], 170))
# print(check_eligibility([85, 90], 170))
# print(check_eligibility([85, 95], 168))
# print(check_eligibility([112, 97], 185))
# print(check_eligibility([110, 102, 90, 106], 222))
# print(check_eligibility([106, 99, 90, 88], 205))
# print(check_eligibility([106, 99, 103, 96], 227))