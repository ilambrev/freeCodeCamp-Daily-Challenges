from datetime import datetime

def can_retake(finish_time, current_time):
    date_format = "%Y-%m-%dT%H:%M:%S"
    time_to_retake_in_hours = 48
    finish_time_date = datetime.strptime(finish_time, date_format)
    current_time_date = datetime.strptime(current_time, date_format)

    diff_in_hours = (current_time_date.timestamp() - finish_time_date.timestamp()) / 3600

    return diff_in_hours >= time_to_retake_in_hours

# print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00"))
# print(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00"))
# print(can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00"))
# print(can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59"))