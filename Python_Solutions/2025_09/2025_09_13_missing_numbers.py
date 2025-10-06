def find_missing_numbers(arr):
    arr.sort()
    missing_numbers = [num for num in range(1, arr[-1] + 1) if num not in arr]
    
    return missing_numbers

# print(find_missing_numbers([1, 3, 5]))
# print(find_missing_numbers([1, 2, 3, 4, 5]))
# print(find_missing_numbers([1, 10]))
# print(find_missing_numbers([10, 1, 10, 1, 10, 1]))
# print(find_missing_numbers([3, 1, 4, 1, 5, 9]))
# print(find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]))