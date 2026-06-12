from math import factorial

def get_itinerary_count(stops):
    return factorial(len(stops)) * (2 * len(stops) - 3)

# print(get_itinerary_count(["library", "park"]))
# print(get_itinerary_count(["library", "park", "arcade"]))
# print(get_itinerary_count(["library", "park", "arcade", "store"]))
# print(get_itinerary_count(["library", "park", "arcade", "store", "cafe"]))
# print(get_itinerary_count(["library", "park", "arcade", "store", "cafe", "market", "museum"]))