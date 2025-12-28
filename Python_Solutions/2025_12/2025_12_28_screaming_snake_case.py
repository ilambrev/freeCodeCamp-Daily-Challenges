from string import ascii_uppercase

def to_screaming_snake_case(variable_name):
    result = variable_name

    if "-" in variable_name:
        result = variable_name.replace("-", "_")
    elif any((c in ascii_uppercase) for c in variable_name):
        result = variable_name[0] + "".join(
            ["_" + variable_name[i] if variable_name[i] in ascii_uppercase else variable_name[i] for i in range(1, len(variable_name))])

    return result.upper()

# print(to_screaming_snake_case("userEmail"))
# print(to_screaming_snake_case("UserPassword"))
# print(to_screaming_snake_case("user_id"))
# print(to_screaming_snake_case("user-address"))
# print(to_screaming_snake_case("username"))