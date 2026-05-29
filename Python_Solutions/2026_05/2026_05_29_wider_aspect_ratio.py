def get_wider_aspect_ratio(a, b):
    def find_devisor(width, height):
        width_divisors = []
        height_divisors = []

        for i in range(1, min(width, height) + 1):

            if width % i == 0:
                width_divisors.append(i)
            
            if height % i == 0:
                height_divisors.append(i)
            
        return max(list(set(width_divisors) & set(height_divisors)))
    
    width_a, height_a = (int(n) for n in a.split("x"))
    width_b, height_b = (int(n) for n in b.split("x"))

    divisor_a = find_devisor(width_a, height_a)
    divisor_b = find_devisor(width_b, height_b)

    ratio_a = [int(width_a / divisor_a), int(height_a / divisor_a)]
    ratio_a_value = ratio_a[0] / ratio_a[1]
    ratio_b = [int(width_b / divisor_b), int(height_b / divisor_b)]
    ratio_b_value = ratio_b[0] / ratio_b[1]

    return f"{ratio_a[0]}:{ratio_a[1]}" if ratio_a_value >= ratio_b_value else f"{ratio_b[0]}:{ratio_b[1]}"

# print(get_wider_aspect_ratio("1920x1080", "800x600"))
# print(get_wider_aspect_ratio("1080x1350", "2048x1536"))
# print(get_wider_aspect_ratio("640x480", "2440x1220"))
# print(get_wider_aspect_ratio("360x640", "1080x1920"))
# print(get_wider_aspect_ratio("3440x1440", "2048x858"))
# print(get_wider_aspect_ratio("12345x61234", "12534x51234"))