def get_cleanup_score(items):
    item_scores = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38
    }

    score = 0
    counter = 0
    strike = 0
    previous_item = ""

    for item in items:
        counter += 1
        multiplier = 1 + int(counter / 5) if counter % 5 == 0 else 1
        
        if "rare" in item:
            score += int(item[1]) * multiplier
            strike = 0
            previous_item = item[0]
        else:
            item_score = item_scores[item]

            if item == previous_item:
                strike += 1
                item_score += strike
            elif previous_item:
                strike = 0

            previous_item = item
            
            score += item_score * multiplier

    return score

# print(get_cleanup_score(["bottle", "straw", "shoe", "battery"]))
# print(get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]))
# print(get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]))
# print(get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]))
# print(get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"]))