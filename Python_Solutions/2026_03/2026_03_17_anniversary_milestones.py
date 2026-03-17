def get_milestone(years):
    milestones = [
        [1, "Paper"],
        [5, "Wood"],
        [10, "Tin"],
        [25, "Silver"],
        [40, "Ruby"],
        [50, "Gold"],
        [60, "Diamond"],
        [70, "Platinum"]
    ]

    if years < milestones[0][0]:
        return "Newlyweds"
    else:
        for years_married, milestone in milestones[::-1]:
            if years >= years_married:
                return milestone

# print(get_milestone(0))
# print(get_milestone(1))
# print(get_milestone(8))
# print(get_milestone(10))
# print(get_milestone(26))
# print(get_milestone(45))
# print(get_milestone(50))
# print(get_milestone(64))
# print(get_milestone(71))