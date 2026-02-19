def avalanche_risk(snow_depth, slope):
    slope_values = {
        "Gentle": {"Shallow": "Safe", "Moderate": "Safe", "Deep": "Safe"},
        "Steep": {"Shallow": "Safe", "Moderate": "Risky", "Deep": "Risky"},
        "Very Steep": {"Shallow": "Safe", "Moderate": "Risky", "Deep": "Risky"}
    }
    
    return slope_values.get(slope).get(snow_depth)

# print(avalanche_risk("Shallow", "Gentle"))
# print(avalanche_risk("Shallow", "Steep"))
# print(avalanche_risk("Shallow", "Very Steep"))
# print(avalanche_risk("Moderate", "Gentle"))
# print(avalanche_risk("Moderate", "Steep"))
# print(avalanche_risk("Moderate", "Very Steep"))
# print(avalanche_risk("Deep", "Gentle"))
# print(avalanche_risk("Deep", "Steep"))
# print(avalanche_risk("Deep", "Very Steep"))