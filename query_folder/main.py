from flask import Flask, json, jsonify, request

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query_route():
    id = request.args.get('id')
    return query_db(id)


def query_db(query):
    with open("/data/db.json")as infile:
        data = json.load(infile)

    for id, recipe in data.items():
        if id == query:
            return data[id]


    return "Not found"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5007)