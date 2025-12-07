def compress_string(sentence):
    words = sentence.split()

    counter = 1
    current_word = words[0]

    result = []

    for i in range(1, len(words)):
        if words[i] == current_word:
            counter += 1
        
        if not words[i] == current_word:
            if counter > 1:
                result.append(f"{current_word}({counter})")
            else:
                result.append(current_word)
            
            current_word = words[i]
            counter = 1
    
    if counter > 1:
        result.append(f"{current_word}({counter})")
    else:
        result.append(current_word)

    return " ".join(result)

# print(compress_string("yes yes yes please"))
# print(compress_string("I have have have apples"))
# print(compress_string("one one three and to the the the the"))
# print(compress_string("route route route route route route tee tee tee tee tee tee"))