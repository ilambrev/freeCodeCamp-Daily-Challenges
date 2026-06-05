def is_valid_schema(obj):
    roles = ["user", "creator", "moderator", "staff", "admin"]

    def is_list_of_strings(v):
        return isinstance(v, list) and len([s for s in v if not isinstance(s, str)]) == 0

    pairs = list(obj.items())

    if len(pairs) < 5:
        return False

    result = True

    for i in range(min(6, len(pairs))):
        k, v = pairs[i]

        if i == 0:
            result = result and (k == "username" and isinstance(v, str))
        elif i == 1:
            result = result and (k == "posts" and (type(v) is int))
        elif i == 2:
            result = result and (k == "verified" and isinstance(v, bool))
        elif i == 3:
            result = result and (k == "role" and v in roles)
        
        if i == 4:
            if k == "supporter":
                result = result and isinstance(v, bool) and len(pairs) > 5
            elif k == "badges":
                result = result and is_list_of_strings(v)
                break
            else:
                result = False

        if i == 5:
            result = result and (k == "badges" and is_list_of_strings(v))
        
        if not result:
            break

    return result

# print(is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False, "badges": ["early-adopter", "popular"]}))
# print(is_valid_schema({"username": "tonya", "posts": 299, "verified": True, "role": "moderator", "supporter": True, "badges": ["streak-master", "veteran"], "followers": 1233}))
# print(is_valid_schema({"username": "zara", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}))
# print(is_valid_schema({"username": "nicole", "posts": 65, "verified": True, "role": "admin", "supporter": False, "badges": ["first-post", 18]}))
# print(is_valid_schema({"username": "tim", "posts": 25, "verified": True, "role": "staff", "supporter": False}))
# print(is_valid_schema({"username": "charlie", "posts": 0, "verified": False, "role": "user", "supporter": "no", "badges": ["first-post", "anniversary"]}))
# print(is_valid_schema({"username": "wanda", "posts": 15, "verified": True, "role": "friend", "supporter": True, "badges": ["popular"]}))
# print(is_valid_schema({"username": "guy", "posts": 5, "verified": "false", "role": "staff", "supporter": True, "badges": ["helper"]}))
# print(is_valid_schema({"username": "carrie", "verified": True, "role": "moderator", "supporter": True, "badges": ["helper", "sharer"]}))
# print(is_valid_schema({"username": True, "posts": 75, "verified": True, "role": "creator", "supporter": True, "badges": ["veteran"]}))