from datetime import datetime

def get_rental_cost(rented, returned, tier):
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    due_back_time_seconds = 12 * 3600
    tiers = {
        1: {"cost": 4.99, "fee": 3.99},
        3: {"cost": 3.99, "fee": 2.99},
        7: {"cost": 2.99, "fee": 0.99},
    }

    total_cost = 0.0

    cost = tiers[tier]["cost"]
    fee = tiers[tier]["fee"]

    rented_date = datetime.strptime(rented, date_format)
    returned_date = datetime.strptime(returned, date_format)
    over_days = (returned_date.date() - rented_date.date()).days - tier
    returned_date_time_seconds = returned_date.hour * 3600 + returned_date.minute * 60 + returned_date.second

    if over_days >= 0 and returned_date_time_seconds > due_back_time_seconds:
        over_days += 1

    total_cost += cost + max(over_days, 0) * fee

    return f"${total_cost:.2f}"

# print(get_rental_cost("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1))
# print(get_rental_cost("2026-06-18T14:30:00Z", "2026-06-20T12:30:00Z", 1))
# print(get_rental_cost("2026-06-18T10:15:00Z", "2026-06-18T19:45:00Z", 3))
# print(get_rental_cost("2026-06-18T15:20:00Z", "2026-06-23T08:10:00Z", 3))
# print(get_rental_cost("2026-06-18T12:00:00Z", "2026-06-25T12:00:00Z", 7))
# print(get_rental_cost("2026-06-18T08:00:00Z", "2027-06-18T14:00:00Z", 7))