def tribonacci_sequence(start_sequence, length):
    sequence = []

    if length < 4:
        sequence = start_sequence[:length]
    else:
        sequence += start_sequence
        for i in range(3, length):
            next_element = sequence[i - 3] + sequence[i - 2] + sequence[i - 1]
            sequence.append(next_element)

    return sequence

# print(tribonacci_sequence([0, 0, 1], 20))
# print(tribonacci_sequence([21, 32, 43], 1))
# print(tribonacci_sequence([0, 0, 1], 0))
# print(tribonacci_sequence([10, 20, 30], 2))
# print(tribonacci_sequence([10, 20, 30], 3))
# print(tribonacci_sequence([123, 456, 789], 8))