def is_valid_equation(equation):
    equation_parts = equation.replace("=", "").split()
    expected_result = int(equation_parts.pop())
    operations = {
        "+": lambda op1, op2: op1 + op2,
        "-": lambda op1, op2: op1 - op2,
        "*": lambda op1, op2: op1 * op2,
        "/": lambda op1, op2: op1 / op2 if op2 !=0 else 0
    }
    high_priority_operation = "*/"
    low_priority_operations = "+-"

    high_priority_operation_indexes = [i for i in range(len(equation_parts)) if equation_parts[i] in high_priority_operation]
    low_priority_operations_indexes = [i for i in range(len(equation_parts)) if equation_parts[i] in low_priority_operations]
    operations_indexes = high_priority_operation_indexes + low_priority_operations_indexes
    
    operations_result = 0

    for i in range(len(operations_indexes)):
        operation_index = operations_indexes[i]
        op1 = int(equation_parts[operation_index-1])
        op2 = int(equation_parts[operation_index+1])
        operation = equation_parts[operation_index]

        if i == 1 and operation_index == 3:
            op1 = operations_result
        elif i == 1 and operation_index == 1:
            op2 = operations_result

        operations_result = operations[operation](op1, op2)

    return expected_result == operations_result

# print(is_valid_equation("2 + 2 = 4"))
# print(is_valid_equation("2 + 3 - 1 = 4"))
# print(is_valid_equation("8 / 2 = 4"))
# print(is_valid_equation("10 * 5 = 50"))
# print(is_valid_equation("2 - 2 = 0"))
# print(is_valid_equation("2 + 9 / 3 = 5"))
# print(is_valid_equation("20 - 2 * 3 = 14"))
# print(is_valid_equation("2 + 5 = 6"))
# print(is_valid_equation("10 - 2 * 3 = 24"))
# print(is_valid_equation("3 + 9 / 3 = 4"))