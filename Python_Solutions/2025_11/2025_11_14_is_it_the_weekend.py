import calendar

def days_until_weekend(date_string):
    year, month, day = map(int, date_string.split("-"))

    day_index = calendar.weekday(year, month, day)

    if day_index == 5 or day_index == 6:
        return "It's the weekend!"
    else:
        days = 5 - day_index
        return f"{days} {'days' if days > 1 else 'day'} until the weekend."

# print(days_until_weekend("2025-11-14"))
# print(days_until_weekend("2025-01-01"))
# print(days_until_weekend("2025-12-06"))
# print(days_until_weekend("2026-01-27"))
# print(days_until_weekend("2026-09-07"))
# print(days_until_weekend("2026-11-29"))