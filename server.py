from flask import Flask, request,jsonify
import utilty

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : utility.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/predict_home_price',methods = ['POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    no_of_rooms = int(request.form['no_of_rooms'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': utility.get_estimated_price(location,sqft,no_of_rooms,bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
   print('Starting Python Flask Server for Home Price Prediction...')
   app.run()