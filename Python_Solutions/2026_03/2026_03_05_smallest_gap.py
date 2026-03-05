def smallest_gap(s):
    smallest_gap = s
    for i in range(len(s) - 1):
        index = s.find(s[i], i + 1)
        if index > -1 and len(s[i+1:index]) < len(smallest_gap):
            smallest_gap = s[i+1:index]

    return smallest_gap

# print(smallest_gap("ABCDAC"))
# print(smallest_gap("racecar"))
# print(smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4"))
# print(smallest_gap("Hello World"))
# print(smallest_gap("The quick brown fox jumps over the lazy dog."))