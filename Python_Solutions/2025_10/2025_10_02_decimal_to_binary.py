def to_binary(decimal):
    binary_number_bits = []

    while decimal > 0:
        remainder = decimal % 2
        binary_number_bits.append(remainder)
        decimal = int(decimal / 2)

    return ''.join([str(number) for number in binary_number_bits[::-1]])

# print(to_binary(5))
# print(to_binary(12))
# print(to_binary(50))
# print(to_binary(99))