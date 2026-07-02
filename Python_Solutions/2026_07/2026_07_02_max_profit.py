def get_max_profit(prices, budget):
    max_profit = 0

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices), 1):
            shares = int(budget / prices[i])
            acquisition_value = shares * prices[i]
            profit = shares * prices[j] - acquisition_value
            if profit > max_profit:
                max_profit = profit

    return f"{max_profit:.2f}"

# print(get_max_profit([5, 6], 50))
# print(get_max_profit([8, 2, 5, 10], 20))
# print(get_max_profit([4, 5, 3, 6], 20))
# print(get_max_profit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200))
# print(get_max_profit([15.38, 15.01, 14.99, 14.62, 14.28], 80))
# print(get_max_profit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25))