import random
from flask import Flask

app = Flask(__name__)

@app.route('/price', methods=['POST'])
def price_route():

    return prices()

def prices():
    cost = random.randrange(100,1000,1) / 100.0
    return("$" + str(cost))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5004)