def is_valid_schema(obj):
    roles = ["user", "creator", "moderator", "staff", "admin"]

    pairs = list(obj.items())

    if len(pairs) < 4:
        return False

    result = True

    for i in range(min(5, len(pairs))):
        k, v = pairs[i]
        if i == 0:
            result = result and (k == "username" and isinstance(v, str))
        elif i == 1:
            result = result and (k == "posts" and (type(v) is int))
        elif i == 2:
            result = result and (k == "verified" and isinstance(v, bool))
        elif i == 3:
            result = result and (k == "role" and v in roles)
        elif i == 4:
            result = result and (k == "supporter" and isinstance(v, bool))

    return result

# print(is_valid_schema({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True}))
# print(is_valid_schema({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"}))
# print(is_valid_schema({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55}))
# print(is_valid_schema({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"}))
# print(is_valid_schema({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True}))
# print(is_valid_schema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False}))
# print(is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True}))
# print(is_valid_schema({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False}))