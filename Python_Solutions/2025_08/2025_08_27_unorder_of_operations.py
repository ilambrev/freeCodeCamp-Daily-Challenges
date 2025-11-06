def evaluate(numbers, operators):
    result = numbers[0] if len(operators) > 0 else 0

    for i in range(0, len(numbers) - 1):
        operator = operators[i % len(operators)]
        operand = numbers[i + 1]

        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand
        elif operator == "*":
            result *= operand
        elif operator == "/":
            result /= operand
        elif operator == "%":
            result %= operand

    return int(result)

# print(evaluate([5, 6, 7, 8, 9], ['+', '-']))
# print(evaluate([17, 61, 40, 24, 38, 14], ['+', '%']))
# print(evaluate([20, 2, 4, 24, 12, 3], ['*', '/']))
# print(evaluate([11, 4, 10, 17, 2], ['*', '*', '%']))
# print(evaluate([33, 11, 29, 13], ['/', '-']))