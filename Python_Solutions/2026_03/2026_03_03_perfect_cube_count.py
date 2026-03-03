def count_perfect_cubes(a, b):
    low, high = sorted([a, b])
    counter = 0

    n_positive = 0
    n_negative = -1

    while True:
        cube = n_positive ** 3
        if low <= cube <= high:
            counter += 1
        elif cube > high:
            break
        n_positive += 1

    while True:
        cube = n_negative ** 3
        if low <= cube <= high:
            counter += 1
        elif cube < low:
            break
        n_negative -= 1

    return counter

# print(count_perfect_cubes(3, 30))
# print(count_perfect_cubes(1, 30))
# print(count_perfect_cubes(30, 0))
# print(count_perfect_cubes(-64, 64))
# print(count_perfect_cubes(9214, -8127))