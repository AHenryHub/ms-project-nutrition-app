from flask import Flask, jsonify, request
from  login import login



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


if __name__ == '__main__':
    app.run(debug=True)