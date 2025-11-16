import random

def generate_hex(color):
    colors = ["red", "green", "blue"]

    if color not in colors:
        return "Invalid color"

    codes = list(range(16, 100))
    random.shuffle(codes)
    colors_codes = codes[0:2]

    list.sort(colors_codes)

    for i in range(2):
        colors_codes[i] = f"{colors_codes[i]:x}".upper()
    
    color_code = ""

    if color == "red":
        color_code += "FF" + colors_codes[0] + colors_codes[1]
    elif color == "green":
        color_code += colors_codes[0] + "FF" + colors_codes[1]
    elif color == "blue":
        color_code += colors_codes[0] + colors_codes[1] + "FF"

    return color_code

# print(generate_hex("yellow"))
# print(generate_hex("red"))
# print(generate_hex("red"))
# print(generate_hex("red"))
# print(generate_hex("red"))
# print(generate_hex("green"))
# print(generate_hex("blue"))