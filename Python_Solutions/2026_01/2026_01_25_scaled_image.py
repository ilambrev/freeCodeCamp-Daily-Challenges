def scale_image(size, scale):
    w, h = size.split("x")
    w = int(int(w) * scale)
    h = int(int(h) * scale)

    return f"{w}x{h}"

# print(scale_image("800x600", 2))
# print(scale_image("100x100", 10))
# print(scale_image("1024x768", 0.5))
# print(scale_image("300x200", 1.5))