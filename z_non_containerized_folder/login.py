from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login_route():
    
    #ata = {"username": username, "password": username}

    username = request.args.get('username')
    password = request.args.get('password')

    return login(username, password)

def login(username, password):
    # login logic
    
    return {"username": username, "password": password}


if __name__ == '__main__':
    app.run(debug=True)