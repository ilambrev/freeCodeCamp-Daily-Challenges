import re

def string_sum(s):
    
    return sum([int(num) for num in re.findall("\d+", s)])

# print(string_sum("3apples2bananas"))
# print(string_sum("10cats5dogs2birds"))
# print(string_sum("125344"))
# print(string_sum("a1b20c300"))
# print(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"))