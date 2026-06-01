def is_valid_schema(obj):
    k, v = next(iter(obj.items()))

    return isinstance(k, str) and isinstance(v, str)

# print(is_valid_schema({"username": "bob"}))
# print(is_valid_schema({"username": "jen", "posts": 30}))
# print(is_valid_schema({"username": ""}))
# print(is_valid_schema({"username": 7}))
# print(is_valid_schema({"posts": 25}))