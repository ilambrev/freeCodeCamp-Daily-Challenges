def shift_array(arr, n):
    i = n % len(arr)
    arr = arr[i:] + arr[:i]

    return arr

# print(shift_array([1, 2, 3], 1))
# print(shift_array([1, 2, 3], -1))
# print(shift_array(["alpha", "bravo", "charlie"], 5))
# print(shift_array(["alpha", "bravo", "charlie"], -11))
# print(shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15))