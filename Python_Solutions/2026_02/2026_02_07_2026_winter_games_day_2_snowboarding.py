def get_landing_stance(start_stance, rotation):
    if int(rotation / 180) % 2 == 0:
        return start_stance
    else:
        return "Regular" if start_stance == "Goofy" else "Goofy"

# print(get_landing_stance("Regular", 90))
# print(get_landing_stance("Regular", 180))
# print(get_landing_stance("Goofy", -270))
# print(get_landing_stance("Regular", 2340))
# print(get_landing_stance("Goofy", 2160))
# print(get_landing_stance("Goofy", -540))