from flask import Flask
import json

def submit(recipe):
    """takes finished recipe and send it to the db"""

    with open("db.json")as infile:
        data = json.load(infile)

    data["4"] = recipe

    
    with open("db.json","w") as outfile:
        json.dump(data, outfile, indent=1)


#test value
#submit({"recipeid":4,"name":"egg","ingredients":{"1":"egg"},"nutrients":{"calories":350,"protein":20,"carbs":45,"fats":10,"added sugar":3}
#      ,"price":1000000.00})