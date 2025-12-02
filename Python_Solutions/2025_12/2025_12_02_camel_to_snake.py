from string import ascii_uppercase

def to_snake(camel):
    snake = ""

    for letter in camel:
        if letter in ascii_uppercase:
            snake += f"_{letter.lower()}"
        else:
            snake += letter

    return snake

# print(to_snake("helloWorld"))
# print(to_snake("myVariableName"))
# print(to_snake("freecodecampDailyChallenges"))