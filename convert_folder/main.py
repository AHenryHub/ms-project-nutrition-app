from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/converter', methods=['POST'])
def converter_route():
    measurement = request.args.get('measurement')
    unit = request.args.get('unit')
    value = request.args.get('value')

    return convert(measurement,unit,value)


def convert(measurement,unit,raw_value):
    
    value = float(raw_value)

    if(measurement=="mass"):
        if(unit=="ounce"):
            return jsonify({"value": value * 28.3})
        if(unit=="gram"):
            return jsonify({"value": value / 28.3})
    #    
    if(measurement=="volume"):
        if(unit=="ounce"):
            return jsonify({"value": value / 33.8})
        if(unit=="liter"):
            return jsonify({"value": value * 33.8})
    #
    if(measurement=="temperature"):
        if(unit=="fahrenheit"):
            return jsonify({"value": (value - 32) / 1.8})
        if(unit=="celsius"):
            return jsonify({"value": (value * 1.8) + 32})
    
    return jsonify({"value": "error"})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5002)