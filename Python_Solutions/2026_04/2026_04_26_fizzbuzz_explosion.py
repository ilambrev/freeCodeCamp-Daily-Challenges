def explode_fizzbuzz(target_z_count):
    initial_string = "fizzbuzz"
    temp_string = ""
    z_count = initial_string.count("z")
    counter = 0

    while z_count < target_z_count:
        for i in range(1, len(initial_string) + 1):
            replacement = ""

            if i % 5 == 0 and i % 3 == 0:
                replacement = "fizzbuzz"
            elif i % 5 == 0:
                replacement = "buzz"
            elif i % 3 == 0:
                replacement = "fizz"

            if replacement:
                temp_string += replacement
            else:
                temp_string += initial_string[i-1]

        initial_string = temp_string
        temp_string = ""
        z_count = initial_string.count("z")
        counter += 1

    return counter

# print(explode_fizzbuzz(9))
# print(explode_fizzbuzz(15))
# print(explode_fizzbuzz(51))
# print(explode_fizzbuzz(52))
# print(explode_fizzbuzz(359))
# print(explode_fizzbuzz(789))
# print(explode_fizzbuzz(54482))
# print(explode_fizzbuzz(1000000))