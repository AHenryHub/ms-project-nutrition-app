import random
from flask import Flask

app = Flask(__name__)

@app.route('/tax', methods=['POST'])
def tax_route():

    return taxes()

def taxes():
    tax = random.randrange(100,1000,1) / 100.0
    return(str(tax) + "%")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5005)