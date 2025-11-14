def find_duplicates(arr):
    unique_values = set()
    duplicated_values = set()

    for num in arr:
        if num in unique_values and not num in duplicated_values:
            duplicated_values.add(num)
        else:
            unique_values.add(num)

    return sorted(list(duplicated_values))

# print(find_duplicates([1, 2, 3, 4, 5]))
# print(find_duplicates([1, 2, 3, 4, 1, 2]))
# print(find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]))