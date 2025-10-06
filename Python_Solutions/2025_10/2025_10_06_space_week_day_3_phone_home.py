def send_message(route):
    speed_km_sec = 300_000
    delay_sec = 0.5
    distance = sum(route)
    satellites_count = len(route) - 1
    transmission_time = (distance / speed_km_sec) + satellites_count * delay_sec

    return round(transmission_time, 4)

# print(send_message([300000, 300000]))
# print(send_message([384400, 384400]))
# print(send_message([54600000, 54600000]))
# print(send_message([1000000, 500000000, 1000000]))
# print(send_message([10000, 21339, 50000, 31243, 10000]))
# print(send_message([802101, 725994, 112808, 3625770, 481239]))