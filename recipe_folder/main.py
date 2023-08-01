from flask import Flask, json, request
import random

app = Flask(__name__)
    
@app.route('/recipe', methods=['POST'])
def recipe_route():
    recipename = request.args.get('name')
    ingredients = request.args.get('ingredients')   #comma separated list
    calories = request.args.get('calories')
    protein = request.args.get('protein')
    fats = request.args.get('fat')
    carbos = request.args.get('carbos')
    sugar = request.args.get('added sugar')
    return upload(recipename,ingredients,calories,protein,fats,carbos,sugar), 200


def upload(recipename,ingredients,calories,protein,fats,carbos,sugar):
    recipe = {
        "recipeid": 0,
        "name": recipename,
        "ingredients": {str(i+1): ingredient for i, ingredient in enumerate(ingredients.split(','))},
        "nutrients": {
            "calories": calories,
            "protein": protein,
            "fats": fats,
            "carbs": carbos,
            "added sugar": sugar
        },
        "price": "$" + str(random.randrange(100,1000,1) / 100.0)     #if we had more time, would figure out post requests, but hard coded for demonstrative purposes
    }
    
    #equivalent function call:
    #submit_db_entry.submit(recipe)

    with open("/data/db.json")as infile:
        data = json.load(infile)

    new_key = len(data) + 1
    recipe["recipeid"] = new_key


    data[str(new_key)] = recipe

    
    with open("/data/db.json","w") as outfile:
        json.dump(data, outfile, indent=1)

    return "thumbs_up"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5008)