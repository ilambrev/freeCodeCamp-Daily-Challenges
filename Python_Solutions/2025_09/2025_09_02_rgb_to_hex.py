def rgb_to_hex(rgb):
    colors = rgb.replace('rgb(', '').replace(')', '').split(', ')

    return '#' + ''.join([f'{int(color):02x}' for color in colors])

# print(rgb_to_hex("rgb(255, 255, 255)"))
# print(rgb_to_hex("rgb(1, 11, 111)"))
# print(rgb_to_hex("rgb(173, 216, 230)"))
# print(rgb_to_hex("rgb(79, 123, 201)"))