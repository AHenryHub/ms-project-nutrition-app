import random
from flask import Flask
import query_db


def prices(recipeid):

    recipe = query_db.query_db(recipeid)

    ingredients = recipe["ingredients"]

    for i in ingredients:
        cost = random.randrange(100,500,1) / 100.0
        print(ingredients[i] + " $" + str(cost))

prices(4)