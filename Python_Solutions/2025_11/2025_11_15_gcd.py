def gcd(x, y):
    smaller_num = min(x, y)
    gcd_num = 1

    for i in range(smaller_num, 0, -1):
        if x % i == 0 and y % i == 0:
            gcd_num = i
            break 

    return gcd_num

# print(gcd(4, 6))
# print(gcd(20, 15))
# print(gcd(13, 17))
# print(gcd(654, 456))
# print(gcd(3456, 4320))