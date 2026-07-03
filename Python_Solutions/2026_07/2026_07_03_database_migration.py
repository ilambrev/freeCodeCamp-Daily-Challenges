def migrate_record(schema, record):
    data = {}
    for field_name in schema:
        if not field_name in record:
            data[field_name] = schema[field_name]
        else:
            data[field_name] = record[field_name]
    for field_name in record:
        if not field_name in data:
            data[field_name] = record[field_name]

    return data

# print(migrate_record({ "username": "", "posts": 0 }, { "verified": True }))  # should return { "username": "", "posts": 0, "verified": True }
# print(migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "posts": 5 }))  # should return { "username": "camper", "posts": 5 }
# print(migrate_record({ "username": "", "posts": 0, "verified": False }, { "username": "camper" }))  # should return { "username": "camper", "posts": 0, "verified": False }
# print(migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "role": "admin" }))  # should return { "username": "camper", "role": "admin", "posts": 0 }
# print(migrate_record({ "username": "", "email": "", "posts": 0, "verified": False, "role": "user", "banned": False }, { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin" }))  # should return { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin", "posts": 0, "verified": False, "banned": False }