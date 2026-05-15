def is_mirror_image(s1, s2):
    symmetric_characters = "WTYUIOHAXVMwoxv08=+:|-_*^!. "
    mirrored_pairs = {
        "[": "]",
        "{": "}",
        "<": ">",
        "b": "d",
        "p": "q",
        "(": ")",
        "]": "[",
        "}": "{",
        ">": "<",
        "d": "b",
        "q": "p",
        ")": "("
    }

    if not len(s1) == len(s2):
        return False

    for i in range(len(s1)):
        s1_symbol = s1[i]
        s2_symbol = s2[-i-1]

        is_pair_mirrored = s1_symbol in mirrored_pairs and s2_symbol == mirrored_pairs[s1_symbol]
        is_pair_symmetric = s1_symbol == s2_symbol and s1_symbol in symmetric_characters

        if not (is_pair_mirrored or is_pair_symmetric):
            return False

    return True

# print(is_mirror_image("[HOW]", "[WOH]"))
# print(is_mirror_image("MOM", "MOM"))
# print(is_mirror_image("vow", "wov"))
# print(is_mirror_image("TIM", "TIM"))
# print(is_mirror_image("{WOW}", "}WOW{"))
# print(is_mirror_image("XXVII", "IIV%X"))
# print(is_mirror_image("><(((*>", "<*)))><"))
# print(is_mirror_image("WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()", "()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW"))