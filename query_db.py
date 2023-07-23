import json


def query_db(query):
    f = open('db.json')

    data = json.load(f)

    for i in data:
        print(i)
        if json.loads(i) == query:
            f.close()
            return data[i]

    f.close()


print(query_db(1))
