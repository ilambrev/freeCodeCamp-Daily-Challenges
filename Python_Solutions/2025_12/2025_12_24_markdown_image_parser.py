def parse_image(markdown):
    alt_text, url = markdown[2:-1].split("](")

    return f'<img src="{url}" alt="{alt_text}">'

# print(parse_image("![Cute cat](cat.png)"))
# print(parse_image("![Rocket Ship](https://freecodecamp.org/cdn/rocket-ship.jpg)"))
# print(parse_image("![Cute cats!](https://freecodecamp.org/cats.jpeg)"))