from invokes import invoke_http
from flask import Flask, request, jsonify
import os, json
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/swap", methods = ['GET'])
def swap():
    from_amount = request.args.get('from_amount')
    from_currency = request.args.get("from_currency")
    to_currency = request.args.get("to_currency")

    from_price_URL = f"http://127.0.0.1:5001/coin/{from_currency}"
    to_price_URL = f"http://127.0.0.1:5001/coin/{to_currency}"
    email = ""

    conversion_ratio = getRatio(from_price_URL, to_price_URL)

    # Retrieves wallet balance 
    

    conversion_amount = float(from_amount) * float(conversion_ratio) * float(0.99)

    #Updates wallet

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
def callWallet(from_currency, to_currency, user_email):
    pass 

if __name__ == "__main__":
    app.run(port=5004, debug=True)
