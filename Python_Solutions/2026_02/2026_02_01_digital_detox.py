from datetime import datetime

def digital_detox(logs):
    min_login_interval_seconds = 14400
    max_logins_number = 2

    logs_by_date = {}

    for log in logs:
        date, time = log.split()
        if date not in logs_by_date:
            logs_by_date[date] = []
        logs_by_date[date].append(time)

    if [d for d in logs_by_date if len(logs_by_date[d]) > max_logins_number]:
        return False
    
    logs_by_time = []

    for log in logs:
        log_parts = log.split()

        year, month, day = log_parts[0].split("-")
        hours, minutes, seconds = log_parts[1].split(":")

        current_datetime = datetime(int(year), int(month), int(day), int(hours), int(minutes), int(seconds))
        logs_by_time.append(current_datetime.timestamp())
    
    logs_by_time.sort()

    for i in range(1, len(logs_by_time)):
        if logs_by_time[i] - logs_by_time[i-1] < min_login_interval_seconds:
            return False

    return True

# print(digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
# print(digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]))
# print(digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
# print(digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]))
# print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
# print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))