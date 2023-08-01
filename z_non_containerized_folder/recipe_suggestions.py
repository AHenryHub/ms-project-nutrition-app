from flask import Flask, json



with open('db.json') as f:
    data = json.load(f)

def suggest(available_ingredients):

    available_ingredients_set  = set(available_ingredients)

    # ing = input("Enter the ingredient you want to use: ")
    matches = []

    for id, recipe in data.items():
        first_ingredient = recipe['ingredients']['1']

        if first_ingredient in available_ingredients_set:
            matches.append(recipe)

    return matches

print(suggest(['egg']))

