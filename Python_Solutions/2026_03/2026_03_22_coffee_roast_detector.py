def detect_roast(beans):
    bean_types = {
        "'": 1,
        "-": 2,
        ".": 3
    }

    beans_by_type = [bean_types[bean] for bean in beans]
    roast_level = sum(beans_by_type) / len(beans_by_type)

    if roast_level <= 1.74:
        return "Light"
    elif roast_level <= 2.5:
        return "Medium"
    else:
        return "Dark"

# print(detect_roast("''-''''''-'-''--''''"))
# print(detect_roast(".'-''-''..'''.-.-''-"))
# print(detect_roast("--.''--'-''.--..-.--"))
# print(detect_roast("-...'-......-..-...-"))
# print(detect_roast(".--.-..-......----.'"))
# print(detect_roast("..-..-..-..-....-.-."))
# print(detect_roast("-'-''''''..-'.''-'.'"))