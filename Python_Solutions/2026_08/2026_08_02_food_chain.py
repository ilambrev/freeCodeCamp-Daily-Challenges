def get_food_chain(pairs):

    def find_predator_index(predator):
        for i in range(len(pairs)):
            if pairs[i][0] == predator:
                return i
        return -1

    predators = set()
    preys = set()

    for pair in pairs:
        predator, prey = pair
        predators.add(predator)
        preys.add(prey)

    predator = [p for p in predators if p not in preys][0]
    chain = []

    for i in range(len(pairs)):
        chain.append(predator)
        index = find_predator_index(predator)
        if index == -1:
            break
        predator = pairs[index][1]

    chain.append(predator)

    return chain

# print(get_food_chain([["cat", "mouse"]]))
# print(get_food_chain([["wolf", "deer"], ["deer", "grass"]]))
# print(get_food_chain([["hawk", "snake"], ["snake", "frog"], ["frog", "fly"]]))
# print(get_food_chain([["rabbit", "grass"], ["fox", "rabbit"], ["eagle", "fox"]]))
# print(get_food_chain([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]]))