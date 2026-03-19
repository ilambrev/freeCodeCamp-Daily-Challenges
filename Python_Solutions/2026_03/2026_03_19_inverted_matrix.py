def invert_matrix(matrix):
    distinct_values = []

    for row in matrix:
        for item in row:
            if item not in distinct_values:
                distinct_values.append(item)
            if len(distinct_values) == 2:
                break
        
        if len(distinct_values) == 2:
            break
    
    v1, v2 = distinct_values
    
    for row in matrix:
        for i in range(len(row)):
            row[i] = v2 if row[i] == v1 else v1

    return matrix

# print(invert_matrix([["a", "b"], ["a", "a"]]))
# print(invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]))
# print(invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]]))
# print(invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]]))
# print(invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]))