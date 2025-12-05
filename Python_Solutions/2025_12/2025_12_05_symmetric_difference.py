def difference(arr1, arr2):
    symmetric_difference = []

    for el in arr1:
        if not el in arr2:
            symmetric_difference.append(el)

    for el in arr2:
        if not el in arr1:
            symmetric_difference.append(el)

    return symmetric_difference

# print(difference([1, 2, 3], [3, 4, 5]))
# print(difference(["a", "b"], ["c", "b"]))
# print(difference([1, "a", 2], [2, "b", "a"]))
# print(difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))