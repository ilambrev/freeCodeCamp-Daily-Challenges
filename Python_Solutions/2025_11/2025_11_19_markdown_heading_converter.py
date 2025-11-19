import re

def convert(heading):
    pattern = r"^ *(#{1,6})( +)[^ ]*.*$"
    result = "Invalid format"

    matches = re.findall(pattern, heading)

    if matches:
        result = heading.lstrip()
        result = re.sub(matches[0][1], "", result, count=1)
        result = result.replace(matches[0][0], f"<h{len(matches[0][0])}>") + f"</h{len(matches[0][0])}>"
    
    return result

# print(convert("# My level 1 heading"))
# print(convert("My heading"))
# print(convert("##### My level 5 heading"))
# print(convert("#My heading"))
# print(convert("  ###  My level 3 heading"))
# print(convert("####### My level 7 heading"))
# print(convert("## My #2 heading"))