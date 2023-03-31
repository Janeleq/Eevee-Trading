# Price Microservice to show different CC prices on diff cc pages
from flask import Flask, redirect, render_template, url_for, jsonify
import requests
from flask_cors import CORS
import os

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')
CORS(app)

# invoke Crytocompare API to get different pricing according to specific CC

@app.route("/BNB")
def binance():
    return render_template('coins/bnb.html')

@app.route("/BTC")
def bitcoin():
    return render_template('coins/btc.html')

@app.route("/ADA")
def cardano():
    return render_template('coins/ada.html')

@app.route("/DOGE")
def doge():
    return render_template('coins/doge.html')

@app.route("/ETH")
def ethereum():
    return render_template('coins/eth.html')

@app.route("/<string:coin>/price")
def find_price(coin):
        print("\nReceived an coin for conversion in JSON:", coin)
        if coin == 'BNB':
            getBNBSinglePrice()
        elif coin == 'ADA':
            getADASinglePrice()
        elif coin == 'SOL':
            getSOLSinglePrice()
        elif coin == 'BTC':
            getBTCSinglePrice()
        elif coin == 'DOGE':
            getDOGESinglePrice()
        elif coin == 'ETH':
            getETHSinglePrice()
            

def getSOLSinglePrice():
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for SOL: {price}USD")

    if requests.get(singlePriceUrl) != "":
        price = response.json()["USD"]
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving SOL price"
        }
    ), 404
    


def getBNBSinglePrice():
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=BNB&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for BNB: {price}USD")

    if price:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving BNB price"
        }
    ), 404


def getBTCSinglePrice():
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for BTC: {price}USD")

    if price:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving BTC price"
        }
    ), 404



def getADASinglePrice():
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=ADA&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for ADA: {price}USD")

    if price:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving ADA price"
        }
    ), 404



def getDOGESinglePrice():
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for DOGE: {price}USD")

    if price:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving DOGE price"
        }
    ), 404

def getETHSinglePrice():
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for ETH: {price}USD")

    if price:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving ETH price"
        }
    ), 404
    
with app.app_context():
     print(getSOLSinglePrice())
     print(getETHSinglePrice())
     print(getADASinglePrice())
     print(getDOGESinglePrice())
     print(getBTCSinglePrice())
     print(getBNBSinglePrice())

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(port=5001, debug=True)
