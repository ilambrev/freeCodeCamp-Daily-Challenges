def get_allergen_friendly_meals(meals, allergens):
    def is_sutable(meal_allergens, allergens):
        for allergen in meal_allergens:
            if allergen in allergens:
                return False
        
        return True

    return [m[0] for m in meals if is_sutable(m[1], allergens)]

# print(get_allergen_friendly_meals([["pasta", ["wheat", "milk"]], ["salad", ["nuts"]]], ["milk"]))
# print(get_allergen_friendly_meals([["steak", ["soy"]], ["fried rice", []], ["fish tacos", ["fish", "wheat"]], ["chicken parmesan", ["wheat", "milk"]]], ["soy", "fish"]))
# print(get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["eggs", "milk"]))
# print(get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["wheat", "nuts"]))