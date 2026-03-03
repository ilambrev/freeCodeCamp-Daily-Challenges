def is_flat(arr):

    return len([el for el in arr if isinstance(el, list)]) == 0

# print(is_flat([1, 2, 3, 4]))
# print(is_flat([1, [2, 3], 4]))
# print(is_flat([1, 0, False, True, "a", "b"]))
# print(is_flat(["a", [0], "b", True]))
# print(is_flat([1, [2, [3, [4, [5]]]], 6]))