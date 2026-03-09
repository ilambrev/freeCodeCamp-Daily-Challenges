import re

def is_valid_hsl(hsl):
    pattern = re.compile("^hsl\( *(\d{1,3}) *, *(\d{1,3})% *, *(\d{1,3})% *\) *;?$")
    matches = pattern.match(hsl)

    if matches is not None:
        is_hue_valid = 0 <= int(matches.group(1)) <= 360
        is_saturation_valid = 0 <= int(matches.group(2)) <= 100
        is_lightness_valid = 0 <= int(matches.group(3)) <= 100

        return is_hue_valid and is_saturation_valid and is_lightness_valid
    else:
        return False

# print(is_valid_hsl("hsl(240, 50%, 50%)"))
# print(is_valid_hsl("hsl( 200 , 50% , 75% )"))
# print(is_valid_hsl("hsl(99,60%,80%);"))
# print(is_valid_hsl("hsl(0, 0%, 0%) ;"))
# print(is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;"))
# print(is_valid_hsl("hsl(361, 50%, 80%)"))
# print(is_valid_hsl("hsl(300, 101%, 70%)"))
# print(is_valid_hsl("hsl(200, 55%, 75)"))
# print(is_valid_hsl("hsl (80, 20%, 10%)"))