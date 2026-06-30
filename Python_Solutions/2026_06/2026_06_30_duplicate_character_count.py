def duplicate_character_count(str1, str2):

    return len([s for s in str2 if s in str1])

# print(duplicate_character_count("aloha", "hei"))
# print(duplicate_character_count("jambo", "bonjour"))
# print(duplicate_character_count("hello", "hola"))
# print(duplicate_character_count("ola", "hej"))
# print(duplicate_character_count("ciao", "konnichiwa"))
# print(duplicate_character_count("merhaba", "xin chao"))
# print(duplicate_character_count("hello world", "hello to everyone around the world"))