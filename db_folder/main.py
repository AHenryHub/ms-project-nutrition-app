from flask import Flask,request,jsonify, Response
import json

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_route():
    recipe = request.args.get('recipe')
    return submit(json.loads(recipe)),  200

def submit(recipe):
    """takes finished recipe and send it to the db"""

    with open("/data/db.json")as infile:
        data = json.load(infile)


    new_key = len(data) + 1
    recipe["recipeid"] = new_key

#    data.pop('None',None)

    data[str(new_key)] = recipe

    
    with open("/data/db.json","w") as outfile:
        json.dump(data, outfile, indent=1)

    return "thumbs_up"

@app.route('/resub', methods=['POST'])
def resub_route():

    recipe = request.args.get('recipe')
    id = request.args.get('id')
    print(recipe,flush=True)
    return resubmit(recipe, id), 200


def resubmit(recipe, id):
    """takes finished recipe and send it to the db"""
    
    with open("/data/db.json")as infile:
        data = json.load(infile)

    data[str(id)] = recipe
    print(recipe,flush=True)
    print(data[str(id)],flush=True)
    print(data["1"],flush=True)

    with open("/data/db.json","w") as outfile:
        json.dump(data, outfile, indent=1)

    return "okay"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5001)

#test value
#submit({"recipeid":4,"name":"egg","ingredients":{"1":"egg"},"nutrients":{"calories":350,"protein":20,"carbs":45,"fats":10,"added sugar":3}
#      ,"price":1000000.00})