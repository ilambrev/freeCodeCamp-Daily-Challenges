import re

def extract_attributes(element):
    attributes = re.findall("[a-z]+=\"[\w -]+\"", element)

    for i in range(len(attributes)):
        attributes[i] = ", ".join(attributes[i].replace('"', "").split("="))

    return attributes

# print(extract_attributes('<span class="red"></span>'))
# print(extract_attributes('<meta charset="UTF-8" />'))
# print(extract_attributes("<p>Lorem ipsum dolor sit amet</p>"))
# print(extract_attributes('<input name="email" type="email" required="true" />'))
# print(extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>'))