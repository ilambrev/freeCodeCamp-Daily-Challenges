def buy_items(funds, items):
    exchange_rates = {
        "USD": 	1.00,
        "EUR": 	1.10,
        "GBP": 	1.25,
        "JPY": 	0.0070,
        "CAD": 	0.75
    }

    funds_usd = float(funds[0]) * exchange_rates[funds[1]]
    items_usd = [float(item[0]) * exchange_rates[item[1]] for item in items]

    bought_items = 0

    for item in items_usd:
        if funds_usd - item >= 0:
            funds_usd -= item
            bought_items += 1
        else:
            break

    if bought_items == len(items_usd):
        return "Buy them all!"
    else:
        return f"Buy the first {bought_items} items."

# print(buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]))
# print(buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]))
# print(buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]))
# print(buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]]))
# print(buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]))