def to_12(time):
    hours = int(time[:2])
    minutes = time[2:]
    part_of_day = "AM"

    if hours > 11:
        hours -= 12
        part_of_day = "PM"
    
    if hours == 0:
        hours = 12

    return f"{hours}:{minutes} {part_of_day}"

# print(to_12("1124"))
# print(to_12("0900"))
# print(to_12("1455"))
# print(to_12("2346"))
# print(to_12("0030"))