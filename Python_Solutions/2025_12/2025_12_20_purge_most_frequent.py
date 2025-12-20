def purge_most_frequent(arr):
    elements = {}

    for element in arr:
        if element not in elements:
            elements[element] = 0
        
        elements[element] += 1
    
    sorted_elements = sorted(elements.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    elements_to_remove = [element for element in sorted_elements if element[1] == sorted_elements[0][1]]

    for element_to_remove in elements_to_remove:
        arr = [element for element in arr if not element == element_to_remove[0]]

    return arr

# print(purge_most_frequent([1, 2, 2, 3]))
# print(purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]))
# print(purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]))
# print(purge_most_frequent([5, 5, 5, 5]))