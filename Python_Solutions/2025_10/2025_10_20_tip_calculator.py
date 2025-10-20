def calculate_tips(meal_price, custom_tip):
    price = float(meal_price[1:])
    percentage = float(custom_tip[:-1])

    return [f"${(price * 0.15):.2f}", f"${(price * 0.20):.2f}", f"${(price * percentage / 100):.2f}"]

# print(calculate_tips("$10.00", "25%"))
# print(calculate_tips("$89.67", "26%"))
# print(calculate_tips("$19.85", "9%"))