import re

def parse_bold(markdown):
    pattern = r"(?:\*{2}(?:(?:[A-Za-z][A-Za-z ]*[A-Za-z])|[A-Za-z]+)\*{2})|(?:_{2}(?:(?:[A-Za-z][A-Za-z ]*[A-Za-z])|[A-Za-z]+)_{2})"

    matches = re.findall(pattern, markdown)

    if matches:
        for match in matches:
            new_str = "<b>" + match[2:-2] + "</b>"
            markdown = markdown.replace(match, new_str)

    return markdown

# print(parse_bold("**This is bold**"))
# print(parse_bold("__This is also bold__"))
# print(parse_bold("**This is not bold **"))
# print(parse_bold("__ This is also not bold__"))
# print(parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog."))