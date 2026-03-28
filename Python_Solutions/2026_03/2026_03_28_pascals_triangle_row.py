def pascal_row(n):
    triangle = [[1], [1, 1]]

    for i in range(2, n):
        above_row = triangle[i-1]
        new_row = []
        for j in range(i + 1):
            if j == 0:
                new_row.append(above_row[0])
            elif j == i:
                new_row.append(above_row[i-1])
            else:
                new_row.append(above_row[j-1] + above_row[j])
        triangle.append(new_row)

    return triangle[n-1]

# print(pascal_row(5))
# print(pascal_row(3))
# print(pascal_row(1))
# print(pascal_row(10))
# print(pascal_row(15))