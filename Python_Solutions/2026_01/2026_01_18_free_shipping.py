def gets_free_shipping(cart, minimum):
    items_prices = {
        "shirt": 34.25,
        "jeans": 48.50,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95
    }
    
    return sum([items_prices[item] for item in cart]) >= minimum

# print(gets_free_shipping(["shoes"], 50))
# print(gets_free_shipping(["hat", "socks"], 50))
# print(gets_free_shipping(["jeans", "shirt", "jacket"], 75))
# print(gets_free_shipping(["socks", "socks", "hat"], 75))
# print(gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100))
# print(gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200))