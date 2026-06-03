def is_valid_schema(obj):
    roles = ["user", "creator", "moderator", "staff", "admin"]

    pairs = list(obj.items())

    if len(pairs) < 4:
        return False

    result = True

    for i in range(4):
        k, v = pairs[i]
        if i == 0:
            result = result and (k == "username" and isinstance(v, str))
        elif i == 1:
            result = result and (k == "posts" and isinstance(v, int))
        elif i == 2:
            result = result and (k == "verified" and isinstance(v, bool))
        elif i == 3:
            result = result and (k == "role" and v in roles)

    return result

# print(is_valid_schema({"username": "henry", "posts": 0, "verified": True, "role": "staff"}))
# print(is_valid_schema({"username": "sara", "posts": 45, "verified": False, "role": "creator", "followers": 70}))
# print(is_valid_schema({"username": "penelope", "posts": 20, "verified": True, "role": "admin"}))
# print(is_valid_schema({"username": "kevin", "posts": 0, "verified": False, "role": "user"}))
# print(is_valid_schema({"username": "george", "posts": 15, "verified": True, "role": "moderator"}))
# print(is_valid_schema({"username": "david", "posts": 0, "verified": False, "role": "guest"}))
# print(is_valid_schema({"username": "wendy", "posts": 10, "verified": True}))
# print(is_valid_schema({"username": "fabian", "posts": 1, "verified": True, "role": True}))
# print(is_valid_schema({"username": 8, "posts": 1, "verified": True, "role": "user"}))
# print(is_valid_schema({"username": "penny", "posts": "10", "verified": True, "role": "staff"}))
# print(is_valid_schema({"username": "john", "posts": "1", "verified": "true", "role": "admin"}))