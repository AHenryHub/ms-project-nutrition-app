from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/menu', methods=['POST'])
def menu_route():

    choice = request.args.get('choice')

    return menu(choice)

def menu(choice):

    options = {
        'menu':{'url':'https://hub.docker.com/r/ahenrycoding/menu','description':'Lists image urls and a basic description of a service.'},
        'login':{'url':'https://hub.docker.com/r/ahenrycoding/login','description':'Takes username and password and returns them.'},
        'recipe':{'url':'https://hub.docker.com/r/ahenrycoding/recipe','description':'Builds a recipe to submit to database.'},
        'nutrition':{'url':'https://hub.docker.com/r/ahenrycoding/nutrition','description':'Updates macronutrient values for existing recipe.'},
        'price':{'url':'https://hub.docker.com/r/ahenrycoding/price','description':'Assigns a random price to the recipe.'},
        'tax':{'url':'https://hub.docker.com/r/ahenrycoding/tax','description':'Assigns a random sales tax for the recipe.'},
        'submitdb':{'url':'https://hub.docker.com/r/ahenrycoding/submitdb','description':'Takes a recipe and submits it to the database.'},
        'query':{'url':'https://hub.docker.com/r/ahenrycoding/query','description':'Searches the database for a given key and returns the value.'},
        'suggest':{'url':'https://hub.docker.com/r/ahenrycoding/suggest','description':'Searches the database for recipes starting with a given ingredient and returns those as a list.'},
        'convert':{'url':'https://hub.docker.com/r/ahenrycoding/convert','description':'Converts a common cooking/baking measurement to and from Metric and Imperial systems and returns the new value.'}
        }
    for key, value in options.items():
        if choice == key:
            return options[choice]
        
    return "Not found"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5009)