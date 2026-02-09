def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    results = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]
    results.sort(reverse=True)
    player_result = distance_points + style_points + wind_comp + k_point_bonus
    result = "No Medal"

    if player_result > results[0]:
        result = "Gold"        
    elif player_result > results[1]:
        result = "Silver"
    elif player_result > results[2]:
        result = "Bronze"

    return result

# print(ski_jump_medal(125.0, 58.0, 0.0, 6.0))
# print(ski_jump_medal(119.0, 50.0, 1.0, 4.0))
# print(ski_jump_medal(122.0, 52.0, -1.0, 4.0))
# print(ski_jump_medal(118.0, 50.5, -1.5, 4.0))
# print(ski_jump_medal(124.0, 50.5, 2.0, 5.0))
# print(ski_jump_medal(119.0, 49.5, 0.0, 3.0))