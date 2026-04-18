def do_math(s):
    digit_indexes = [i for i in range(len(s)) if s[i].isdigit()]

    if len(digit_indexes) == 1:
        return int(s[digit_indexes[0]])

    result = 0
    number = s[digit_indexes[0]]
    isFirstNumber = True
    index_difference = 0

    for i in range(1, len(digit_indexes)):
        digit = s[digit_indexes[i]]
        current_index_difference = digit_indexes[i] - digit_indexes[i-1] - 1
        if current_index_difference == 0:
            number += digit
            continue
        
        if isFirstNumber:
            result += int(number)
            isFirstNumber = False
        elif index_difference % 2 == 0:
            result += int(number)     
        else:
            result -= int(number)

        index_difference = current_index_difference
        number = digit
    
    if index_difference % 2 == 0:
        result += int(number)
    else:
        result -= int(number)
            
    return result

# print(do_math("3ab10c8"))
# print(do_math("6MINUS4"))
# print(do_math("9plus3"))
# print(do_math("5fkwo#10i#%.<>15P=@20!#B/25"))
# print(do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt"))