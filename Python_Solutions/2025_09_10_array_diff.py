def array_diff(arr1, arr2):
    united_arr = arr1 + arr2
    result = sorted([value for value in united_arr 
                     if not (value in arr1 and value in arr2)])

    return result

# print(array_diff(["apple", "banana"], ["apple", "banana", "cherry"]))
# print(array_diff(["apple", "banana", "cherry"], ["apple", "banana"]))
# print(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]))
# print(array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]))
# print(array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]))