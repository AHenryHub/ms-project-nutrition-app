from flask import Flask, jsonify, request
from  login import login
from converter import convert


app = Flask(__name__)


@app.route('/', methods=['GET'])
def bottle():
    data = {"dummy": "5"}
    return jsonify(data)

@app.route('/login', methods=['POST'])
def login_route():
    
    #ata = {"username": username, "password": username}

    username = request.args.get('username')
    password = request.args.get('password')

    return login(jsonify(username, password))


@app.route('/converter', methods=['GET'])
def converter_route():
    value = request.args.get('value')
    unit = request.args.get('unit')
    measurement = request.args.get('measurement')
    return convert(measurement,unit,value)



if __name__ == '__main__':
    app.run(debug=True)