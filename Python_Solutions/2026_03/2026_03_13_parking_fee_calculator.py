from math import ceil

def time_to_minutes(time):
    hours, minutes = (int(n) for n in time.split(":"))

    return minutes + hours * 60

def calculate_parking_fee(park_time, pickup_time):
    hour_fee = 3
    overnight_fee = 10
    minimum_fee = 5

    park_time_minutes = time_to_minutes(park_time)
    pickup_time_minutes = time_to_minutes(pickup_time)

    total_fee = 0

    if pickup_time_minutes >= park_time_minutes:
        total_fee = ceil((pickup_time_minutes - park_time_minutes) / 60) * hour_fee
    else:
        total_fee += overnight_fee
        total_fee += ceil(24 - abs(park_time_minutes - pickup_time_minutes) / 60) * hour_fee

    return f"${total_fee if total_fee >= minimum_fee else minimum_fee}"

# print(calculate_parking_fee("09:00", "11:00"))
# print(calculate_parking_fee("10:00", "10:30"))
# print(calculate_parking_fee("08:10", "10:45"))
# print(calculate_parking_fee("14:40", "23:10"))
# print(calculate_parking_fee("18:15", "01:30"))
# print(calculate_parking_fee("11:11", "11:10"))