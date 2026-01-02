def nth_fibonacci(n):
    if n == 1:
        return 0

    if n == 2:
        return 1

    nums = [0, 1]

    for i in range(2, n):
        nums.append(nums[i - 1] + nums[i - 2])

    return nums[-1]

# print(nth_fibonacci(4))
# print(nth_fibonacci(10))
# print(nth_fibonacci(15))
# print(nth_fibonacci(40))
# print(nth_fibonacci(75))