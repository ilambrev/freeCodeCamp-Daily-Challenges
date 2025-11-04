def image_search(images, term):
    result = []

    for image in images:
        if term.lower() in image.lower():
            result.append(image)

    return result

# print(image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog"))  # should return ["dog.png"]
# print(image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun"))  # should return ["Sunset.jpg", "sunflower.jpeg"]
# print(image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG"))  # should return ["Moon.png", "stars.png"]
# print(image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat"))  # should return ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"]