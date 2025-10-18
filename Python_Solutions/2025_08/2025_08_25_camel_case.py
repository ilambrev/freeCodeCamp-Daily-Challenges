import re

def to_camel_case(s):
    res = re.split(r'[-_\s]+', s.lower())

    return res[0] + "".join([word.capitalize() for word in res[1:]])

# print(to_camel_case("hello world"))
# print(to_camel_case("HELLO WORLD"))
# print(to_camel_case("secret agent-X"))
# print(to_camel_case("FREE cODE cAMP"))
# print(to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"))