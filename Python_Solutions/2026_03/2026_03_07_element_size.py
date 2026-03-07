def get_element_size(window_size, element_vw, element_vh):
    width, height = window_size.split(" x ")

    new_width = int(int(width) * (int(element_vw.replace("vw", "")) / 100))
    new_height = int(int(height) * (int(element_vh.replace("vh", "")) / 100))
    
    return f"{new_width} x {new_height}"

# print(get_element_size("1200 x 800", "50vw", "50vh"))
# print(get_element_size("320 x 480", "25vw", "50vh"))
# print(get_element_size("1000 x 500", "7vw", "3vh"))
# print(get_element_size("1920 x 1080", "95vw", "100vh"))
# print(get_element_size("1200 x 800", "0vw", "0vh"))
# print(get_element_size("1440 x 900", "100vw", "114vh"))