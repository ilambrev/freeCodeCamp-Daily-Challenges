def fizz_buzz_count(start, end):
    counter = {"fizz": 0, "buzz": 0}
    
    for i in range(start, end + 1):
        if i % 5 == 0:
            counter["buzz"] += 1
        if i % 3 == 0:
            counter["fizz"] += 1

    return counter

# print(fizz_buzz_count(1, 11))
# print(fizz_buzz_count(14, 41))
# print(fizz_buzz_count(24, 100))
# print(fizz_buzz_count(-635, -14))
# print(fizz_buzz_count(-5432, 6789))