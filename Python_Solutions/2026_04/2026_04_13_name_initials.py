def get_initials(name):
    initials = [f"{name_part[0].upper()}." for name_part in name.split(" ")]

    return "".join(initials)

# print(get_initials("Tommy Millwood"))
# print(get_initials("Savanna Puddlesplash"))
# print(get_initials("Frances Cowell Conrad"))
# print(get_initials("Dragon"))
# print(get_initials("Dorothy Vera Clump Haverstock Norris"))