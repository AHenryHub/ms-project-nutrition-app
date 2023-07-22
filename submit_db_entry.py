from flask import Flask
import json

def submit(recipe):
    """takes finished recipe and send it to the db"""

    json_obj = json.dumps(recipe, indent=1)

    with open("db.json","w") as outfile:
        outfile.write(json_obj)

submit({"recipeid":"001","name":"spaghetti","ingredients":{"1":"pasta","2":"sauce","3":"oregano","4":"salt","5":"pepper"},"nutrients":{"calories":350,"protein":20,"carbs":45,"fats":10,"added sugar":3}
        ,"price":10.00})