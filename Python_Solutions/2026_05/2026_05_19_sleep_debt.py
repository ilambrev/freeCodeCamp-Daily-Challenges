def sleep_debt(hours_slept, target_hours):
    dept = sum([target_hours - h for h in hours_slept]) + target_hours

    return dept if dept > 0 else 0

# print(sleep_debt([6, 6, 6, 6, 6, 6], 8))  # should return 20
# print(sleep_debt([6, 7, 8, 4, 8, 6], 7))  # should return 10
# print(sleep_debt([10, 10, 9, 10, 9, 11], 9))  # should return 4
# print(sleep_debt([8, 7, 6, 7, 6, 8], 6))  # should return 0
# print(sleep_debt([8, 9, 10, 9, 10, 7], 7))  # should return 0