def sock_pairs(pairs, cycles):
    socks = pairs * 2

    for i in range(1, cycles + 1):
        if i % 2 == 0:
            socks = socks - 1 if socks > 0 else 0

        if i % 3 == 0:
            socks += 1

        if i % 5 == 0:
            socks = socks - 1 if socks > 0 else 0

        if i % 10 == 0:
            socks += 2

    return int(socks / 2)

# print(sock_pairs(2, 5))
# print(sock_pairs(1, 2))
# print(sock_pairs(5, 11))
# print(sock_pairs(6, 25))
# print(sock_pairs(1, 8))