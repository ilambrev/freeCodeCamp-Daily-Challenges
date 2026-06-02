def is_valid_schema(obj):
    pairs = list(obj.items())

    if len(pairs) < 3:
        return False

    result = True

    for i in range(3):
        k, v = pairs[i]
        if i == 0:
            result = result and (k == "username" and isinstance(v, str))
        elif i == 1:
            result = result and (k == "posts" and isinstance(v, int))
        elif i == 2:
            result = result and (k == "verified" and isinstance(v, bool))

    return result

# print(is_valid_schema({"username": "alice", "posts": 10, "verified": False}))  # should return True
# print(is_valid_schema({"username": "carol", "posts": 15, "verified": True, "followers": 25}))  # should return True
# print(is_valid_schema({"username": "frank", "posts": "21", "verified": True}))  # should return False
# print(is_valid_schema({"username": "sam", "posts": 17, "verified": "false"}))  # should return False
# print(is_valid_schema({"username": "bill", "verified": True}))  # should return False
# print(is_valid_schema({"username": "fred", "verified": True}))  # should return False
# print(is_valid_schema({"username": 5, "posts": 10, "verified": True}))  # should return False