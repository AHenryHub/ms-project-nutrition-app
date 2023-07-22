import json


def query_db(query):
    f = open('db.json')

    data = json.loads(f)

    for i in data:
        if json.loads(i)["recipeid"] == query:
            f.close()
            return i

    f.close()


query_db(0)
