from math import floor

def nth_prime(n):
    primes_count = 0
    current_num = 1

    while primes_count < n:
        current_num += 1
        is_num_prime = True

        for i in range(2, floor(current_num / 2) + 1):
            if current_num % i == 0:
                is_num_prime = False
                break

        if is_num_prime:
            primes_count += 1

    return current_num

# print(nth_prime(5))
# print(nth_prime(10))
# print(nth_prime(16))
# print(nth_prime(99))
# print(nth_prime(1000))