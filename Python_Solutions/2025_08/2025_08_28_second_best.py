def get_laptop_cost(laptops, budget):
    unique_prices_sorted = sorted(set(laptops), reverse=True)

    if budget >= unique_prices_sorted[1]:
        return unique_prices_sorted[1]
    else:
        return next((price for price in unique_prices_sorted if price <= budget), 0)
    
# print(get_laptop_cost([1500, 2000, 1800, 1400], 1900))
# print(get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900))
# print(get_laptop_cost([2099, 1599, 1899, 1499], 2200))
# print(get_laptop_cost([2099, 1599, 1899, 1499], 1000))
# print(get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450))