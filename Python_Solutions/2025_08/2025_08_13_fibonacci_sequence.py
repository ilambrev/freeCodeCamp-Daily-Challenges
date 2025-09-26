def fibonacci_sequence(start_sequence, length):
    sequence = []

    if length == 1:
        sequence.append(start_sequence[0])
    elif length >= 2:
        sequence += start_sequence
        for i in range(2, length):
            next_element = sequence[i - 2] + sequence[i - 1]
            sequence.append(next_element)

    return sequence

# print(fibonacci_sequence([0, 1], 20))
# print(fibonacci_sequence([21, 32], 1))
# print(fibonacci_sequence([0, 1], 0))
# print(fibonacci_sequence([10, 20], 2))
# print(fibonacci_sequence([123456789, 987654321], 5))