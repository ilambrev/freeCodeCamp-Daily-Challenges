def is_narcissistic(n):

    return n == sum(int(d) ** len(str(n)) for d in str(n))

# print(is_narcissistic(153))
# print(is_narcissistic(154))
# print(is_narcissistic(371))
# print(is_narcissistic(512))
# print(is_narcissistic(9))
# print(is_narcissistic(11))
# print(is_narcissistic(9474))
# print(is_narcissistic(6549))