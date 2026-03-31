def alarm_check(alarm_time, wake_time):
    def time_to_minutes(time):
        hours, minutes = [int(e) for e in time.split(":")]

        return hours * 60 + minutes

    alarm_time_in_minutes = time_to_minutes(alarm_time)
    wake_time_in_minutes = time_to_minutes(wake_time)

    if wake_time_in_minutes < alarm_time_in_minutes:
        return "early"
    elif wake_time_in_minutes > alarm_time_in_minutes + 10:
        return "late"
    else:
        return "on time"

# print(alarm_check("07:00", "06:45"))
# print(alarm_check("06:30", "06:30"))
# print(alarm_check("08:10", "08:15"))
# print(alarm_check("09:30", "09:45"))
# print(alarm_check("08:15", "08:25"))
# print(alarm_check("05:45", "05:56"))
# print(alarm_check("04:30", "04:00"))