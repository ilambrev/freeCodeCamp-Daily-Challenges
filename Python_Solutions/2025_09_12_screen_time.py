def too_much_screen_time(hours):

    if max(hours) >= 10:
        return True

    if max([sum(hours[i:i + 3]) / 3
            for i in range(len(hours)-2)]) >= 8:
        return True

    if sum(hours) / len(hours) >= 6:
        return True

    return False

# print(too_much_screen_time([1, 2, 3, 4, 5, 6, 7]))
# print(too_much_screen_time([7, 8, 8, 4, 2, 2, 3]))
# print(too_much_screen_time([5, 6, 6, 6, 6, 6, 6]))
# print(too_much_screen_time([1, 2, 3, 11, 1, 3, 4]))
# print(too_much_screen_time([1, 2, 3, 10, 2, 1, 0]))
# print(too_much_screen_time([3, 3, 5, 8, 8, 9, 4]))
# print(too_much_screen_time([3, 9, 4, 8, 5, 7, 6]))