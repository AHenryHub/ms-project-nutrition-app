from flask import Flask, request, json, jsonify
app = Flask(__name__)

@app.route('/nutrition', methods=['POST'])
def nutrition_route():
    recipeid = request.args.get('recipeid')
    calories = request.args.get('calories')
    protein = request.args.get('protein')
    fats = request.args.get('fat')
    carbos = request.args.get('carbos')
    sugar = request.args.get('added sugar')
    return macros(recipeid,calories,protein,fats,carbos,sugar), 200

def macros(recipeid,calories,protein,fats,carbos,sugar):
    nutrition_list = {}

    with open("/data/db.json")as infile:
        data = json.load(infile)

    recipe = data[recipeid]
    
    #lists macro nutrient quantities per serving for an ingredient (macros in grams/serving)
    nutrition_list = {'calories':int(calories),'protein':int(protein),'fats':int(fats),'carbohydrates':int(carbos),'added sugar':int(sugar)}

    #updates the values in db.json
    recipe["nutrients"] = nutrition_list

    return jsonify(recipe)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5003)