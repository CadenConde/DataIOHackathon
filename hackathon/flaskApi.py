from flask import Flask, request, jsonify
from main import setup

app = Flask(__name__)

testCO2, testMPG = None, None

@app.route('/init', methods=['GET'])
def init():
    global testCO2, testMPG
    testMPG, testCO2 = setup()
    return jsonify({"good": True})  # Return as JSON response to confirm the variables are set

@app.route('/predict', methods=['GET'])
def predict():
    # Access query parameters using request.args
    # x_columns = ['Vehicle Class','Engine Size(L)','Cylinders','Transmission','Fuel Type', 'Displacement per Cylinder']

    modelType = request.args.get('type', type=str)  # Get 'engine_size' and convert it to float
    vc = request.args.get('vehicleclass', type=str)  # Get 'engine_size' and convert it to float
    es = request.args.get('enginesize', type=float)        # Get 'cylinders' and convert it to int
    c = request.args.get('cylinders', type=int)        # Get 'cylinders' and convert it to int
    t = request.args.get('transmission', type=str)        # Get 'cylinders' and convert it to int
    ft = request.args.get('fueltype', type=str)        # Get 'cylinders' and convert it to int

    print("!!!!!", modelType, vc, es, c, t, ft)

    if (testCO2 == None or testMPG == None): return jsonify({"result": None})

    res = None
    if modelType == "co2":
        print("it is co2")
        res = testCO2([vc, es, c, t, ft])[0]
    else:
        print("it is NOTTTT co2")
        res = testMPG([vc, es, c, t, ft])[0]
    
    return jsonify({
        "result": res,
    })


if __name__ == '__main__':
    app.run(debug=True)

    # testData=["TWO-SEATER", 6.6, 6, "M7", "N", .5]
    # print(test1(testData))
    # print(test2(testData))
