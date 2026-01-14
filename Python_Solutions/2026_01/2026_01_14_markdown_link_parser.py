import string

def parse_link(markdown):
    url = markdown[markdown.find("(") + 1:markdown.find(")")]
    text = markdown[markdown.find("[") + 1:markdown.find("]")]

    html_template = string.Template('<a href="$url">$text</a>')

    return html_template.substitute(url=url, text=text)

# print(parse_link("[freeCodeCamp](https://freecodecamp.org/)"))
# print(parse_link("[Donate to our charity.](https://www.freecodecamp.org/donate/)"))
# print(parse_link("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)"))