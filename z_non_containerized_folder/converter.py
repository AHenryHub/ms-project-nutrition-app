from flask import Flask, request, Response, jsonify

#unit converter

#1 oz = 28.3 g

#33.8 oz = 1 L

#1 degree fahrenheit = 1.8 * degree celsius + 32
#1 degree celsius = (1 degree fahrenheit - 32) / 1.8


"""
GET - convert one thing to another
Request Body: {
    input type
    input value
    output type
}
Response Body: {
    output value
}

"""

def convert():
    measurement = request.args.get('measurement')
    unit = request.args.get('unit')
    value = float(request.args.get('value'))
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


    