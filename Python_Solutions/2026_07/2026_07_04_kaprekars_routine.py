def kaprekar(n):
    result = n
    counter = 0
    while not result == 6174:
        counter += 1
        digits = [d for d in str(result)]
        largest_num = "".join(sorted(digits, reverse=True))
        smallest_num = "".join(sorted(digits))
        result = int(largest_num) - int(smallest_num)

    return counter

# print(kaprekar(1234))
# print(kaprekar(2025))
# print(kaprekar(7173))
# print(kaprekar(3164))
# print(kaprekar(8082))