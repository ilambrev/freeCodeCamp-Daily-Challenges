def pairwise(arr, target):
    indexes_sum = 0

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                indexes_sum += i + j

    return indexes_sum

# print(pairwise([2, 3, 4, 6, 8], 10))
# print(pairwise([4, 1, 5, 2, 6, 3], 7))
# print(pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20))
# print(pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24))