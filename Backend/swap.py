from invokes import invoke_http
from flask import Flask, request, jsonify
import os, json
import requests
from flask_cors import CORS

import pyrebase

app = Flask(__name__)
CORS(app)

firebase_config = {
    "apiKey": "AIzaSyAUfijsgUQsPpdx5A21wO0wCS1qRkwh5o0",
    "authDomain": "cryptobuds-ba428.firebaseapp.com",
    "databaseURL": "https://cryptobuds-ba428-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "cryptobuds-ba428",
    "storageBucket": "cryptobuds-ba428.appspot.com",
    "messagingSenderId": "72206190161",
    "appId": "1:72206190161:web:bc8dbb3bf116fcc69fda70",
    "measurementId": "G-BVXDMYJR2K"
}
fb = pyrebase.initialize_app(firebase_config)
database = fb.database()

@app.route("/swap", methods = ['GET'])
def swap():
    from_amount = request.args.get('from_amount')
    from_currency = request.args.get("from_currency")
    to_currency = request.args.get("to_currency")

    from_price_URL = f"http://127.0.0.1:5001/coin/{from_currency}"
    to_price_URL = f"http://127.0.0.1:5001/coin/{to_currency}"
    email = ""

    conversion_ratio = getRatio(from_price_URL, to_price_URL)

    gas_fee = 0.01
    if from_currency == to_currency:
        gas_fee = 0 

    conversion_amount = float(from_amount) * float(conversion_ratio) * float(1 - gas_fee)
    to_amount = request.args.get("to_amount")

    #Updates wallet
    updateWallet(from_currency, from_amount, to_currency, to_amount)

    #Status of successful swap
    if conversion_amount:
        #AMQP activity

        return {
            "code": 200,
            'conversion_amount': conversion_amount
        }

    #Status of failed swap
    else:
        #AMQP activity

        return {
            "code": 500,
            "message": "Swap failure sent for error handling."
        }
    
def getPrice(response):
    price = response['data']['price']
    return price

# Obtain rates from price.py and calculates ratio of swap (to rate / from rate)
def getRatio(from_url, to_url):
    
    to_price_data = requests.get(to_url)
    from_price_data = requests.get(from_url)
    from_price = None
    to_price = None
    
    if to_price_data:
        to_price_data = to_price_data.json()
        to_price = getPrice(to_price_data)
    if from_price_data:
        from_price_data = from_price_data.json() 
        from_price = getPrice(from_price_data) 
    return (from_price / to_price)

# Calls wallet to either retrieve or update balance. 
'''
Takes in four arguments - type (retrieve / update), from_currency, to_currency and user_email  
'''
def updateWallet(from_currency, from_amount, to_currency, to_amount):
    coin = None
    wallet_URL = "http://localhost:5100/wallet/" + coin
    # Calls access_wallet to update from_amount
    coin = from_currency
    amount_owned = requests.get(wallet_URL, timeout=10)
    

    # Calls access_wallet to update to_amount

    # Get new wallet balance for to and from currency

    # Returns new wallet balance for to and from currency
    updated_from_balance = None
    updated_to_balance = None
    
    return {
        from_currency : updated_from_balance,
        to_currency : updated_to_balance
    }

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__))
    app.run(port=5004, debug=True)
