def count(text, parameter):
    counter = 0

    for i in range(len(text) - len(parameter) + 1):
        if text[i:i+len(parameter)] == parameter:
            counter += 1

    return counter

# print(count('abcdefg', 'def'))
# print(count('hello', 'world'))
# print(count('mississippi', 'iss'))
# print(count('she sells seashells by the seashore', 'sh'))
# print(count('101010101010101010101', '101'))