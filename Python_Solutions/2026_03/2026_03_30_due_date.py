import datetime

def get_due_date(date_str):
    months_to_add = 9
    year, month, day = [int(e) for e in date_str.split("-")]
    new_year = year if month + months_to_add <= 12 else year + 1
    new_month = month + months_to_add if month + \
        months_to_add <= 12 else month + months_to_add - 12
    new_day = 28

    test_date = datetime.datetime(new_year, new_month, new_day)
    next_month = test_date + datetime.timedelta(days=4)
    new_month_last_day = (
        next_month - datetime.timedelta(days=next_month.day)).day

    if day > new_month_last_day:
        new_day = new_month_last_day
    else:
        new_day = day

    return f"{new_year}-{new_month:02}-{new_day:02}"

# print(get_due_date("2025-03-30"))
# print(get_due_date("2025-04-27"))
# print(get_due_date("2025-05-29"))
# print(get_due_date("2026-06-30"))
# print(get_due_date("2026-10-11"))