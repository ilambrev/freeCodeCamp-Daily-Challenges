from string import ascii_uppercase

def sum_letters(s):

    return sum([ascii_uppercase.index(l) + 1 for l in s.upper() if l in ascii_uppercase])

# print(sum_letters("Hello"))
# print(sum_letters("freeCodeCamp"))
# print(sum_letters("The quick brown fox jumps over the lazy dog."))
# print(sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci."))
# print(sum_letters("</404>"))