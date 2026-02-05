def count_change(change):
    cents = sum(change)
    dollars = int(cents / 100)
    cents = cents % 100

    return f"${dollars}.{cents:02}"

# print(count_change([25, 10, 5, 1]))
# print(count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]))
# print(count_change([100, 25, 100, 1000, 5, 500, 2000, 25]))
# print(count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]))
# print(count_change([1]))
# print(count_change([25, 25, 25, 25]))