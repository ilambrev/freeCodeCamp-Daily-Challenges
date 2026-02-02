def groundhog_day_prediction(appearance):
    predictions = [
        "Looks like we'll have six more weeks of winter.",
        "It's going to be an early spring.",
        "No prediction this year."
    ]

    if type(appearance) == bool:
        return predictions[0] if appearance else predictions[1]

    return predictions[2]

# print(groundhog_day_prediction(True))
# print(groundhog_day_prediction(False))
# print(groundhog_day_prediction(None))
# print(groundhog_day_prediction(" "))
# print(groundhog_day_prediction("True"))