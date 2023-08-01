from flask import Flask,request,jsonify, Response
import json

app = Flask(__name__)

@app.route('/suggest', methods=['POST'])
def suggest_route():

    ingredients = request.args.get('ingredients')

    return suggest(ingredients)

def suggest(available_ingredient):

    with open('/data/db.json') as f:
        data = json.load(f)

    matches = []

    for id, recipe in data.items():
        first_ingredient = recipe['ingredients']['1']
        if first_ingredient == available_ingredient:
            matches.append(data[id])

    return matches

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5006)