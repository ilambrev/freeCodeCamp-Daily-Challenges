def format(seconds):
    hours = int(seconds / 3600)
    minutes = int((seconds - (hours * 3600)) / 60)
    remaining_seconds = seconds - (hours * 3600 + minutes * 60)

    if hours > 0:
        return f"{hours}:{minutes:02d}:{remaining_seconds:02d}"
    else:
        return f"{minutes}:{remaining_seconds:02d}"

# print(format(500))
# print(format(4000))
# print(format(1))
# print(format(5555))
# print(format(99999))