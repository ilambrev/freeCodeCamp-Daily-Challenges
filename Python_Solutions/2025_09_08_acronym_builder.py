def build_acronym(s):
    ignored_words = ['a', 'for', 'an', 'and', 'by', 'of']
    words = s.split()

    acronym = ''.join([w[0].upper() for w in words if w not in ignored_words])

    return acronym

# print(build_acronym("Search Engine Optimization"))
# print(build_acronym("Frequently Asked Questions"))
# print(build_acronym("National Aeronautics and Space Administration"))
# print(build_acronym("Federal Bureau of Investigation"))
# print(build_acronym("For your information"))
# print(build_acronym("By the way"))
# print(build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily"))