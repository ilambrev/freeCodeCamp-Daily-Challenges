def capitalize_fibonacci(s):
    fibonacci_numbers = [0, 1]

    while fibonacci_numbers[-1] < len(s):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

    return "".join([s[i].upper() if i in fibonacci_numbers else s[i].lower() for i in range(len(s))])

# print(capitalize_fibonacci("hello world"))
# print(capitalize_fibonacci("HELLO WORLD"))
# print(capitalize_fibonacci("hello, world!"))
# print(capitalize_fibonacci("The quick brown fox jumped over the lazy dog."))
# print(capitalize_fibonacci("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl."))