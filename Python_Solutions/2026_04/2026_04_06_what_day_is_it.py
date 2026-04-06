from datetime import datetime

def get_day_of_week(timestamp):
    week_day = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    return week_day[datetime.fromtimestamp(timestamp / 1000).weekday()]

# print(get_day_of_week(1775492249000))
# print(get_day_of_week(1766246400000))
# print(get_day_of_week(33791256000000))
# print(get_day_of_week(1773576000000))
# print(get_day_of_week(0))