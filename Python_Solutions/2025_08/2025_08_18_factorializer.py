def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial

# print(factorial(0))
# print(factorial(5))
# print(factorial(20))