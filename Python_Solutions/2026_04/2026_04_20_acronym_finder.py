def find_org(acronym):
    organizations = {
        "NASA": "National Avocado Storage Authority",
        "CIA": "Cats Infiltration Agency",
        "FBI": "Fluffy Beanbag Inspectors",
        "DOJ": "Department Of Jelly",
        "WHO": "Wild Honey Organization",
        "EPA": "Eating Pancakes Administration"
    }

    return organizations[acronym] if acronym in organizations else "There is no organization with such an acronym."

# print(find_org("NASA"))
# print(find_org("CIA"))
# print(find_org("FBI"))
# print(find_org("DOJ"))
# print(find_org("WHO"))
# print(find_org("EPA"))