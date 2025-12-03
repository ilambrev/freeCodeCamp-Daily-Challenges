import re

def convert_list_item(markdown):
    pattern = r"^( *[1-9][0-9]*. )(.*)$"

    match = re.search(pattern, markdown)

    if match:
        text = match.group(2)
    else:
        return "Invalid format"

    return "<li>" + text.strip() + "</li>"

# print(convert_list_item("1. My item"))
# print(convert_list_item(" 1.  Another item"))
# print(convert_list_item("1 . invalid item"))
# print(convert_list_item("2. list item text"))
# print(convert_list_item(". invalid again"))
# print(convert_list_item("A. last invalid"))