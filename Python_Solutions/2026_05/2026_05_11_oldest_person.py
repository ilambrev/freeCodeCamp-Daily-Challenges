def get_oldest(people):
    if people:
        sorted_people = [p for p in sorted(people, key=lambda p: -(p['age']))]
        max_age = sorted_people[0]['age']
        return [p['name'] for p in sorted_people if p['age'] == max_age]
    else:
        return people

# print(get_oldest([{ "name": "Brenda", "age": 40 }]))
# print(get_oldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]))
# print(get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }]))
# print(get_oldest([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]))