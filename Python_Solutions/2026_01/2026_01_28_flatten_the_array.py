def flatten(arr):
    flat = []
    for item in arr:
        if isinstance(item, list):
            flat += flatten(item)
        else:
            flat.append(item)
    return flat

# print(flatten([1, [2, 3], 4]))
# print(flatten([5, [4, [3, 2]], 1]))
# print(flatten(["A", [[[["B"]]]], "C"]))
# print(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]))
# print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))