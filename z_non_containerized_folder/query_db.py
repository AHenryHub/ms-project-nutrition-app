import json


def query_db(query):
    f = open('db.json')

    data = json.load(f)

    for i in data:
        if json.loads(i) == query:
            f.close()
            return data[i]

    f.close()
