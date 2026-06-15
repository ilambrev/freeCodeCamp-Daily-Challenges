def is_valid_schema(obj):
    roles = ["user", "creator", "moderator", "staff", "admin"]
    valid_keys = ["username", "posts", "verified", "role", "supporter", "badges"]

    def is_list_of_strings(v):
        return isinstance(v, list) and len([s for s in v if not isinstance(s, str)]) == 0
    
    def is_valid(user_profile, roles):
        pairs = [p for p in list(user_profile.items()) if p[0] in valid_keys]

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
    
    if not next(iter(obj)) == "users":
        return False

    return isinstance(obj["users"], list) and (len(obj["users"]) == 0 or len([profile for profile in obj["users"] if not is_valid(profile, roles)]) == 0)

# print(is_valid_schema({"users": [{"username": "ron", "posts": 14, "verified": True, "role": "creator", "badges": ["early-adopter"]}, {"username": "cher", "posts": 25, "verified": True, "role": "moderator", "supporter": True, "followers": 20, "badges": ["helper"]}]}))
# print(is_valid_schema({"users": []}))
# print(is_valid_schema({"users": {"username": "anne", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}}))
# print(is_valid_schema({"users": [{"username": "tony", "posts": 10, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", 6]}]}))
# print(is_valid_schema({"users": [{"username": "ursula", "posts": 3, "verified": False, "role": "user", "supporter": "false", "badges": ["comeback"]}]}))
# print(is_valid_schema({"users": [{"username": "benny", "posts": 55, "verified": True, "role": "superstar", "supporter": True, "badges": ["veteran"]}]}))
# print(is_valid_schema({"users": [{"username": "chase", "posts": 1, "verified": "yes", "role": "staff", "supporter": False, "badges": ["superstar"]}]}))
# print(is_valid_schema({"users": [{"username": "carla", "posts": "10", "verified": False, "role": "user", "supporter": False, "badges": ["newbie"]}]}))
# print(is_valid_schema({"users": [{"posts": 4, "verified": False, "role": "admin", "supporter": False, "badges": ["superuser", "veteran"]}]}))
# print(is_valid_schema({"users": [{"username": "harold", "posts": 80, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", "hero"]}, {"username": "kim", "posts": 11, "verified": False, "role": "admin", "supporter": True, "badges": ["first"]}, {}]}))