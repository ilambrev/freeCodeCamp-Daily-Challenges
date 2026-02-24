from datetime import date, timedelta

def count_business_days(start, end):
    y, m, d = [int(e) for e in start.split("-")]
    start_date = date(y, m, d)
    y, m, d = [int(e) for e in end.split("-")]
    end_date = date(y, m, d)

    dif = end_date - start_date
    days = dif.days

    current_date = start_date
    business_days = 0

    for i in range(days + 1):
        if current_date.weekday() < 5:
            business_days += 1
        current_date += timedelta(days=1)

    return business_days

# print(count_business_days("2026-02-24", "2026-02-26"))
# print(count_business_days("2026-02-24", "2026-02-28"))
# print(count_business_days("2026-02-21", "2026-03-01"))
# print(count_business_days("2026-03-08", "2026-03-17"))
# print(count_business_days("2026-02-24", "2027-02-24"))