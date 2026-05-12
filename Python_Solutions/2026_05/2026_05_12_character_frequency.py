def get_frequency(s):
    frequency_dic = {}

    for symbol in s:
        frequency_dic[symbol] = frequency_dic.get(symbol, 0) + 1

    return frequency_dic

# print(get_frequency("test"))
# print(get_frequency("mississippi"))
# print(get_frequency("hello world"))
# print(get_frequency("She sells seashells by the seashore."))
# print(get_frequency("The quick brown fox jumps over the lazy dog."))