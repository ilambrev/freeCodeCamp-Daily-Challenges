def get_extension(filename):
    period_index = filename.rfind(".")

    if period_index > -1 and not period_index == len(filename) - 1:
        return filename[period_index + 1:]
    else:
        return "none"

# print(get_extension("document.txt"))
# print(get_extension("README"))
# print(get_extension("image.PNG"))
# print(get_extension(".gitignore"))
# print(get_extension("archive.tar.gz"))
# print(get_extension("final.draft."))