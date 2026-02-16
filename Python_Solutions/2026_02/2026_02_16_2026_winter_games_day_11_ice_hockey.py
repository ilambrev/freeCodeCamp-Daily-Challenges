def get_semifinal_matchups(teams):
    teams_points = []

    for team in teams:
        name, results = team.split(": ")
        results = [int(r) for r in results.split("-")]
        points = 0
        
        for i in range(len(results)):
            points += results[i] * (3 - i)
        
        teams_points.append([name, points])

    semi_final_teams = sorted(teams_points, key=lambda t: t[1], reverse=True)[:4]

    return f"The semi-final games will be {semi_final_teams[0][0]} vs {semi_final_teams[3][0]} and {semi_final_teams[1][0]} vs {semi_final_teams[2][0]}."

# print(get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"]))
# print(get_semifinal_matchups(["CAN: 2-1-1-1", "CZE: 1-1-1-2", "FIN: 1-2-1-1", "NOR: 0-1-1-3", "SLO: 1-0-1-3", "USA: 5-0-0-0"]))
# print(get_semifinal_matchups(["CAN: 3-2-0-0", "CZE: 2-1-2-0", "LAT: 0-0-1-4", "ITA: 1-1-1-2", "DEN: 1-0-0-4", "USA: 3-1-1-0"]))
# print(get_semifinal_matchups(["AUT: 2-2-1-0", "DEN: 1-0-0-4", "ITA: 1-1-1-2", "JPN: 3-2-0-0", "KOR: 2-1-2-0", "LAT: 0-0-1-4"]))