import re

def generate_slug(str):
    allowed_characters = 'abcdefghijklmnopqrstuvwxyz 0123456789'

    str = str.lower().strip()
    str = ''.join([symbol for symbol in str if symbol in allowed_characters])

    str = re.sub('\s+', '%20', str)

    return str

# print(generate_slug("helloWorld"))
# print(generate_slug("hello world!"))
# print(generate_slug(" hello-world "))
# print(generate_slug("hello  world"))
# print(generate_slug("  ?H^3-1*1]0! W[0%R#1]D  "))