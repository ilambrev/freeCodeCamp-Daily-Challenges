def calculate_start_delays(jump_scores):
    multiplier = 1.5
    max_score = max(jump_scores)

    return [0 if d == max_score else round(0.000000001 + (max_score - d) * multiplier) for d in jump_scores]

# print(calculate_start_delays([120, 110, 125]))
# print(calculate_start_delays([118, 125, 122, 120]))
# print(calculate_start_delays([100, 105, 95, 110, 120, 115, 108]))
# print(calculate_start_delays([130, 125, 128, 120, 118, 122, 127, 115, 132, 124]))