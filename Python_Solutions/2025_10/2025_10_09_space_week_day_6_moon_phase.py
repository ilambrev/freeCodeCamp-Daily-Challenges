from datetime import datetime

def moon_phase(date_string):
    reference_date_string = "2000-01-06"
    lunar_cycle_days = 28
    format = '%Y-%m-%d'

    date = datetime.strptime(date_string, format)
    reference_date = datetime.strptime(reference_date_string, format)

    days = ((date - reference_date).days + 1) % lunar_cycle_days

    moon_phase = ""

    if 1 <= days <= 7:
        moon_phase = "New"
    elif 8 <= days <= 14:
        moon_phase = "Waxing"
    elif 15 <= days <= 21:
        moon_phase = "Full"
    elif 22 <= days <= 28:
        moon_phase = "Waning"

    return moon_phase

# print(moon_phase("2000-01-12"))
# print(moon_phase("2000-01-13"))
# print(moon_phase("2014-10-15"))
# print(moon_phase("2012-10-21"))
# print(moon_phase("2022-12-14"))