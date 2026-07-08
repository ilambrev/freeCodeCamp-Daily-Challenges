def triage_issue(ms, message):
    hour_to_ms = 3600000
    day_to_hours = 24
    days = int((ms / hour_to_ms) / day_to_hours)

    if days < 7:
        return "leave it"
    else:
        return "close it" if "bump" in message.lower() else "bump it"

# print(triage_issue(86400000, "Lets fix it"))
# print(triage_issue(1209600000, "still waiting"))
# print(triage_issue(864000000, "bump"))
# print(triage_issue(604800000, "Do we still want this?"))
# print(triage_issue(604800000, "Bumping this"))
# print(triage_issue(345600000, "I'll make a PR"))