def tire_status(pressures_psi, range_bar):
    bar_to_psi = 14.5038
    result = []

    for preasure in pressures_psi:
        preasure_in_bars = preasure / bar_to_psi
        tyre_preasure_condition = "" 

        if preasure_in_bars < range_bar[0]:
            tyre_preasure_condition = "Low"
        elif range_bar[0] <= preasure_in_bars <= range_bar[1]:
            tyre_preasure_condition = "Good"
        elif preasure_in_bars > range_bar[1]:
            tyre_preasure_condition = "High"
        
        result.append(tyre_preasure_condition)

    return result

# print(tire_status([32, 28, 35, 29], [2, 3]))
# print(tire_status([32, 28, 35, 30], [2, 2.3]))
# print(tire_status([29, 26, 31, 28], [2.1, 2.5]))
# print(tire_status([31, 31, 30, 29], [1.5, 2]))
# print(tire_status([30, 28, 30, 29], [1.9, 2.1]))