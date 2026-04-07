def palindrome_locator(s):
    if s == s[::-1]:
        length = len(s)
        half = int(length / 2)

        middle = s[half-1:half+1] if length % 2 == 0 else s[half:half+1]
        
        return middle

    return "none"

# print(palindrome_locator("racecar"))
# print(palindrome_locator("level"))
# print(palindrome_locator("freecodecamp"))
# print(palindrome_locator("noon"))
# print(palindrome_locator("11100111"))