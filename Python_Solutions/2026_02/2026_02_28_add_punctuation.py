import re

def add_punctuation(sentences):
    sentences = re.sub(r" (?=[A-Z])", ". ", sentences)
    
    return sentences + "."

# print(add_punctuation("Hello world"))
# print(add_punctuation("Hello world It's nice today"))
# print(add_punctuation("JavaScript is great Sometimes"))
# print(add_punctuation("A b c D e F g h I J k L m n o P Q r S t U v w X Y Z"))
# print(add_punctuation("Wait.. For it"))