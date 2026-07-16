from string import ascii_lowercase, ascii_uppercase

def pig_latin(s):
    words = s.split()

    def convert_word(word):
        vowels = "aeiou"
        if word[0].lower() in vowels:
            return word + "way"

        is_first_letter_upper_case = word[0] in ascii_uppercase

        consonants_counter = 0

        for letter in word:
            letter_lower_case = letter.lower()
            if letter_lower_case in ascii_lowercase and letter_lower_case not in vowels:
                consonants_counter += 1
            else:
                break

        word = word[consonants_counter:] + word[:consonants_counter].lower() + "ay"

        if is_first_letter_upper_case:
            word = word[0].upper() + word[1:]

        return word

    for i in range(len(words)):
        words[i] = convert_word(words[i])

    return " ".join(words)

# print(pig_latin("universe"))
# print(pig_latin("hello"))
# print(pig_latin("hello universe"))
# print(pig_latin("Hello universe"))
# print(pig_latin("Pig Latin is fun"))
# print(pig_latin("The quick brown fox jumped over the lazy dog"))