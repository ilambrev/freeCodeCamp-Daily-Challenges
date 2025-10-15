def squares_with_three(n):

    return len([number for number in range(1, n + 1) if '3' in str(number ** 2)])

# print(squares_with_three(1))
# print(squares_with_three(10))
# print(squares_with_three(100))
# print(squares_with_three(1000))
# print(squares_with_three(10000))