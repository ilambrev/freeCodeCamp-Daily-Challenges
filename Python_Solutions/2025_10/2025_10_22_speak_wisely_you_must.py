def wise_speak(sentence):
    punctuation_mark = sentence[-1]
    words = sentence.lower()[:-1].split()
    main_words = ["have", "must", "are", "will", "can"]
    index = -1

    for i in range(len(words)):
        if words[i] in main_words:
            index = i
            break

    words[index] = words[index] + punctuation_mark
    words[index + 1] = words[index + 1].capitalize()
    words[-1] = words[-1] + ","
    
    return " ".join(words[index + 1:] + words[:index + 1])

# print(wise_speak("You must speak wisely."))
# print(wise_speak("You can do it!"))
# print(wise_speak("Do you think you will complete this?"))
# print(wise_speak("All your base are belong to us."))
# print(wise_speak("You have much to learn."))