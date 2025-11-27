from datetime import datetime

def calculate_age(birthday):
    date_format = "%Y-%m-%d"

    to_date = datetime.strptime("2025-11-27", date_format)
    birthday_date = datetime.strptime(birthday, date_format)

    years = to_date.year - birthday_date.year

    if to_date.month < birthday_date.month or birthday_date.month and to_date.day < birthday_date.day:
        years -= 1

    return years

# print(calculate_age("2000-11-20"))
# print(calculate_age("2000-12-01"))
# print(calculate_age("2014-10-25"))
# print(calculate_age("1994-01-06"))
# print(calculate_age("1994-12-14"))