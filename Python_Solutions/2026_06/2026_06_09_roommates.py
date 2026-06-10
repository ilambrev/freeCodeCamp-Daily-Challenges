def get_roommates(people):
    roommates = []

    def find_roommates(people):
        group = people[0]["group"]
        people_in_group = [person for person in people if person["group"] == group]
        current_roommates = []

        for i in range(0, len(people_in_group), 2):
            people_in_room = people_in_group[i]["name"]
            people.remove(people_in_group[i])

            if i < len(people_in_group) - 1:
                people_in_room = f"{people_in_room} and {people_in_group[i+1]['name']}"
                people.remove(people_in_group[i+1])
            
            current_roommates.append(people_in_room)

        return current_roommates

    while people:
        current_roommates = find_roommates(people)
        roommates += current_roommates

    return roommates

# print(get_roommates([{ "name": "Alice", "group": "A" }, { "name": "Bob", "group": "B" }, { "name": "Carol", "group": "A" }]))
# print(get_roommates([{ "name": "John", "group": "C" }, { "name": "Julia", "group": "C" }, { "name": "Jim", "group": "C" }]))
# print(get_roommates([{ "name": "Adam", "group": "D" }, { "name": "Abraham", "group": "E" }, { "name": "Austin", "group": "E" }, { "name": "Augustus", "group": "D" }, { "name": "Angelica", "group": "D" }, { "name": "Aaron", "group": "E" }]))
# print(get_roommates([{ "name": "Frank", "group": "A" }, { "name": "Emitt", "group": "B" }, { "name": "Daria", "group": "F" }, { "name": "Charles", "group": "D" }, { "name": "Bailey", "group": "A" }, { "name": "Albert", "group": "F" }]))
# print(get_roommates([{ "name": "Kevin", "group": "A" }, { "name": "Yuri", "group": "A" }, { "name": "Hugo", "group": "B" }, { "name": "Violet", "group": "A" }, { "name": "Brett", "group": "A" }, { "name": "Wayne", "group": "B" }]))