import re

def parse_blockquote(markdown):
    html = re.sub(r"\s*>\s*", "<blockquote>", markdown) + "</blockquote>"
    
    return html

# print(parse_blockquote("> This is a quote"))
# print(parse_blockquote(" > This is also a quote"))
# print(parse_blockquote("  >    So  Is  This"))