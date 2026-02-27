def shift_matrix(matrix, shift):
    row_len = len(matrix[0])

    arr = [num for row in matrix for num in row]

    shift = shift % len(arr)

    if shift > 0:
        arr = arr[len(arr)-shift:] + arr[:len(arr)-shift]
    elif shift < 0:
        arr = arr[shift:] + arr[:shift+1]

    return [arr[i:i+row_len] for i in range(0, len(arr), row_len)]

# print(shift_matrix([[1, 2, 3], [4, 5, 6]], 1))  # should return [[6, 1, 2], [3, 4, 5]]
# print(shift_matrix([[1, 2, 3], [4, 5, 6]], -1))  # should return [[2, 3, 4], [5, 6, 1]]
# print(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))  # should return [[5, 6, 7], [8, 9, 1], [2, 3, 4]]
# print(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6))  # should return [[7, 8, 9], [1, 2, 3], [4, 5, 6]]
# print(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 7))  # should return [[10, 11, 12, 13], [14, 15, 16, 1], [2, 3, 4, 5], [6, 7, 8, 9]]
# print(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54))  # should return [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]]