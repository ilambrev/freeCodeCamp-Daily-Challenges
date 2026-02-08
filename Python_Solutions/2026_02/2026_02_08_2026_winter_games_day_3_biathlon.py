def calculate_penalty_distance(rounds):
    penalty_loop_distance = 150

    return sum([5 - targets_hit for targets_hit in rounds]) * penalty_loop_distance

# print(calculate_penalty_distance([4, 4]))
# print(calculate_penalty_distance([5, 5]))
# print(calculate_penalty_distance([4, 5, 3, 5]))
# print(calculate_penalty_distance([5, 4, 5, 5]))
# print(calculate_penalty_distance([4, 3, 0, 3]))