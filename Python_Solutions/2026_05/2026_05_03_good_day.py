def get_greeting(s):
    hours, minutes = s.split(":")
    time_in_minutes = int(hours) * 60 + int(minutes)

    greeting = "Good night"

    if 300 <= time_in_minutes < 720:
        greeting = "Good morning"
    elif 720 <= time_in_minutes < 1080:
        greeting = "Good afternoon"
    elif 1080 <= time_in_minutes < 1320:
        greeting = "Good evening"

    return greeting

# print(get_greeting("06:30"))
# print(get_greeting("12:00"))
# print(get_greeting("21:59"))
# print(get_greeting("00:01"))
# print(get_greeting("11:30"))