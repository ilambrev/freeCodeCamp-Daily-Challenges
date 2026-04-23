def get_direction(time1, time2):
    day_in_minutes = 24 * 60

    def time_to_minutes(time):
        hours, minutes = time.split(":")

        return int(hours) * 60 + int(minutes)

    time1_in_minutes = time_to_minutes(time1)
    time2_in_minutes = time_to_minutes(time2)

    backward = 0
    forward = 0

    if time1_in_minutes < time2_in_minutes:
        forward = time2_in_minutes - time1_in_minutes
        backward = day_in_minutes - forward
    elif time1_in_minutes > time2_in_minutes:
        backward = time1_in_minutes - time2_in_minutes
        forward = day_in_minutes - backward

    if backward < forward:
        return "backward"
    elif forward < backward:
        return "forward"
    else:
        return "equal"

# print(get_direction("10:00", "12:00"))
# print(get_direction("11:00", "05:00"))
# print(get_direction("00:00", "12:00"))
# print(get_direction("15:45", "01:10"))
# print(get_direction("03:30", "19:50"))
# print(get_direction("06:30", "18:30"))