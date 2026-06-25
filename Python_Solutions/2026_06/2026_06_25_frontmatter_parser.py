import re

def parse_frontmatter(s):
    begin_index = s.find("---\n")
    end_index = s.find("\n---", begin_index + 1)
    dic = {}

    def is_boolean(value):
        return value.lower() == "true" or value.lower() == "false"

    def is_integer(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def parseValue(value):
        if is_boolean(value):
            return eval(value.capitalize())

        if is_integer(value):
            return int(value)

        if is_float(value):
            return float(value)

        return value

    if begin_index > -1 and end_index > -1:
        pairs = s[begin_index+4:end_index].split("\n")

        for pair in pairs:
            key, value = re.split(r":\s+", pair)
            value = parseValue(value)
            dic[key] = value

    return dic

# print(parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---"))
# print(parse_frontmatter("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---"))
# print(parse_frontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---"))
# print(parse_frontmatter("---\nrating: 4.5\nprice: 9.99\n---"))