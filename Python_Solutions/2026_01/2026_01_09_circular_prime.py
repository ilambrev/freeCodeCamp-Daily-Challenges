def is_circular_prime(n):
    def is_not_prime(number):
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                return True

        return False

    digits = [digit for digit in str(n)]

    for i in range(len(digits)):
        if is_not_prime(int("".join(digits))):
            return False

        digits = digits[1:] + digits[0:1]

    return True

# print(is_circular_prime(197))
# print(is_circular_prime(23))
# print(is_circular_prime(13))
# print(is_circular_prime(89))
# print(is_circular_prime(1193))