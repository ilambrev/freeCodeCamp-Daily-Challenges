from string import ascii_letters

def detect_ai(text):
    dashes_count = text.count("-")
    opening_parenthesis_count = text.count("(")
    words = text.split()
    words_with_seven_letters = len([word for word in words if len([letter for letter in word if letter in ascii_letters]) >= 7])

    if dashes_count >= 2 or opening_parenthesis_count >= 2 or words_with_seven_letters >= 3:
        return "AI"
    else:
        return "Human"

# print(detect_ai("The quick brown fox jumped over the lazy dog."))
# print(detect_ai("The hypersonic brown fox - jumped (over) the lazy dog."))
# print(detect_ai("Yes - you're right! I made a mistake there - let me try again."))
# print(detect_ai("The extraordinary students were studying vivaciously."))
# print(detect_ai("The (excited) student was (coding) in the library."))