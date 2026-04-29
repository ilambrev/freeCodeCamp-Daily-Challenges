def parse_url_query(url):
    query_index = url.find("?")
    parameters_data = url[query_index+1:].split("&")
    dict = {}

    for data in parameters_data:
        key, value = data.split("=")
        dict[key] = value

    return dict

# print(parse_url_query("https://example.com/search?name=Alice&age=30"))
# print(parse_url_query("https://freecodecamp.org/learn?skill=programming&language=python"))
# print(parse_url_query("https://freecodecamp.org/items?category=books&sort=asc&page=2"))
# print(parse_url_query("https://example.com?redirect=freecodecamp.org/learn&when=now"))