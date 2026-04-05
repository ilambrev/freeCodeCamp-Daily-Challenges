def get_rotation(n):
    n_as_string = str(n)

    for i in range(len(n_as_string)):
        if int(n_as_string) % len(n_as_string) == 0:
            return i

        n_as_string = n_as_string[1:] + n_as_string[0]

    return "none"

# print(get_rotation(123))
# print(get_rotation(13579))
# print(get_rotation(24681))
# print(get_rotation(84138789345))