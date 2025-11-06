def get_weekday(date_string):
    year, month, day = map(int, date_string.split("-"))

    if month < 3:
        month += 12
        year -= 1

    year_part = year % 100
    century = year // 100

    week_day_index = (day + (13 * (month + 1)) // 5 + year_part + year_part // 4 + century // 4 + 5 * century) % 7
    week_days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    return week_days[week_day_index]

# print(get_weekday("2025-11-06"))
# print(get_weekday("1999-12-31"))
# print(get_weekday("1111-11-11"))
# print(get_weekday("2112-12-21"))
# print(get_weekday("2345-10-01"))