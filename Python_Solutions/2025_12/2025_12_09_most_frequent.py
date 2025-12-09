def most_frequent(arr):
    elements = {}

    for element in arr:
        if not element in elements:
            elements[element] = 0
        
        elements[element] += 1

    return [e[0] for e in sorted(elements.items(), key=lambda item: item[1], reverse=True)][0]

# print(most_frequent(["a", "b", "a", "c"]))
# print(most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]))
# print(most_frequent([True, False, "False", "True", False]))
# print(most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]))