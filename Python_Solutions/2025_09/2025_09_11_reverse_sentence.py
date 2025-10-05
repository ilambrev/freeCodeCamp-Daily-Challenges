def reverse_sentence(sentence):
    words = sentence.split()

    return ' '.join(words[::-1])

# print(reverse_sentence("world hello"))
# print(reverse_sentence("push commit git"))
# print(reverse_sentence("npm  install   apt    sudo"))
# print(reverse_sentence("import    default   function  export"))