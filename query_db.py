import json

def query_db(query):
    f = open('db.json')

    data = json.load(f)

    for i in data:
        if i["recipeid"]==query:
            f.close()
            return i

    f.close()
