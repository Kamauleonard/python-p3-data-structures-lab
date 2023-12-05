spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for spicy in spicy_foods:
        if 'name' in spicy:
            names.append(spicy['name'])

    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for spicy in spicy_foods:
        if 'heat_level' in spicy and spicy['heat_level'] > 5:
            spiciest_foods.append(spicy)

    return spiciest_foods

def print_spicy_foods(spicy_foods):
      for spicy in spicy_foods:
        name = spicy.get('name', '')
        cuisine = spicy.get('cuisine', '')
        heat_level = spicy.get('heat_level', 0)

        heat_emoji = '🌶' * heat_level

        print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy in spicy_foods:
        if 'cuisine' in spicy and spicy['cuisine'] == cuisine:
            return spicy

def print_spiciest_foods(spicy_foods):
    for spicy in spicy_foods:
        heat_level = spicy.get('heat_level', 0)

        if heat_level > 5:
            name = spicy.get('name', '')
            cuisine = spicy.get('cuisine', '')
            heat_emoji = '🌶' * heat_level

            print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")

def get_average_heat_level(spicy_foods):
    total_heat = 0
    count = 0

    for spicy in spicy_foods:
        heat_level = spicy.get('heat_level', 0)
        total_heat += heat_level
        count += 1

    # Avoid division by zero
    if count == 0:
        return 0

    average = total_heat / count
    return round(average)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
