def round_to_nearest_multiple(num, multiple):
    i = 1
    nearest_multiple = num
    while True:
        if (nearest_multiple + i) % multiple == 0:
            nearest_multiple += i
            break

        if (nearest_multiple - i) % multiple == 0:
            nearest_multiple -= i
            break

        i += 1

    return nearest_multiple

# print(round_to_nearest_multiple(5, 3))
# print(round_to_nearest_multiple(17, 4))
# print(round_to_nearest_multiple(43, 5))
# print(round_to_nearest_multiple(38, 11))
# print(round_to_nearest_multiple(93, 12))