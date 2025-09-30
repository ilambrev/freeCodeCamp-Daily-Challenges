def are_anagrams(str1, str2):
    str1_symbols = sorted([symbol for symbol in str1.replace(' ', '').lower()])
    str2_symbols = sorted([symbol for symbol in str2.replace(' ', '').lower()])

    return  str1_symbols == str2_symbols

# print(are_anagrams("listen", "silent"))
# print(are_anagrams("School master", "The classroom"))
# print(are_anagrams("A gentleman", "Elegant man"))
# print(are_anagrams("Hello", "World"))
# print(are_anagrams("apple", "banana"))
# print(are_anagrams("cat", "dog"))