def zip_strings(a, b):
    shortest_length = min(len(a), len(b))
    result = "".join([a[i] + b[i] for i in range(shortest_length)])

    if len(a) == len(b):
        return result
    elif len(a) > len(b):
        return result + a[shortest_length:]
    else:
        return result + b[shortest_length:]

# print(zip_strings("abc", "123"))
# print(zip_strings("acegikmoqsuwy", "bdfhjlnprtvxz"))
# print(zip_strings("day", "night"))
# print(zip_strings("python", "javascript"))
# print(zip_strings("feCdCm", "reoeap"))