from invokes import invoke_http
from flask import Flask, request, jsonify
import os, json
import requests
from flask_cors import CORS
# import amqp_setup
# import pika

import pyrebase

app = Flask(__name__)
CORS(app, origins=['http://localhost:5000'])

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

    conversion_ratio = getRatio(from_price_URL, to_price_URL)
    gas_fee = 0.01
    if from_currency == to_currency:
        gas_fee = 0 

    conversion_amount = float(from_amount) * float(conversion_ratio) * float(1 - gas_fee)
    to_amount = request.args.get("to_amount")

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
            "code": 400,
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

def getNumber(amount_owned,coin):
    amount_owned = amount_owned[coin]
    return amount_owned

# Calls wallet to update balance and retrieve . 
'''
Takes in four arguments - type (retrieve / update), from_currency, to_currency and user_email 
Returns json in format of "updated <coin>" : updated balance 
'''
@app.route("/update?from_currency=<string:from_currency>&from_amount=<string:from_amount>&to_currency=<string:to_currency>&to_amount=<string:to_amount>")
def updateWallet(from_currency, from_amount, to_currency, to_amount):
    coin = None
    wallet_URL = "http://localhost:5100/wallet/{coin}"
    # id = "P2lTOnotbgfpU8ThbATf0Lx6D9G2"

    from_amount = request.args.get('from_amount')
    from_currency = request.args.get("from_currency")
    to_currency = request.args.get("to_currency")
    to_amount = request.args.get("to_amount")
    print(from_amount)
    print(from_currency)
    print(to_currency)
    print(to_amount)

    old_from_balance = None
    old_to_balance = None
    updated_from_balance = None
    updated_to_balance = None
    updated_from_data = None

    # Calls access_wallet to update from_amount and get new balance
    coin = from_currency
    old_from_balance = requests.get(wallet_URL)
    if old_from_balance:
        ownedcoin = old_from_balance.json()
        ownedcoin = getNumber(ownedcoin, coin)
        old_from_balance = ownedcoin
        changed_amt = ownedcoin - from_amount
        updated_from_balance = changed_amt
        database.child("users").child(id).child('wallet_coins').child(to_currency).update({"qty":changed_amt})
        
        # Retrieves updated balance from firebase 
        updated_from_data = database.child("users").child(id).child('wallet_coins').child(from_currency).get()
    
    # transaction, transaction_log, amqp, docker
    # Calls access_wallet to update to_amount and get new balance
    coin = to_currency
    old_to_balance = requests.get(wallet_URL)
    if old_to_balance:
        ownedcoin = updated_to_balance.json()
        ownedcoin = getNumber(ownedcoin, coin)
        old_to_balance = ownedcoin
        changed_amt = ownedcoin + to_amount
        updated_to_balance = changed_amt
        database.child("users").child(id).child('wallet_coins').child(from_currency).update({"qty":changed_amt})

        # Retrieves updated balance from firebase 
        updated_to_data = database.child("users").child(id).child('wallet_coins').child(to_currency).get()

    # Checks db update status and publishes message to rabbitmq
    if updated_from_data != None and updated_to_data != None:
        if updated_to_data.val()['qty'] == updated_to_balance and updated_from_balance.val()['qty'] == updated_from_balance:
            message = jsonify({"success": True, "message": "New to balance updated successfully!"})
            # amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="*", body=message, properties=pika.BasicProperties(delivery_mode = 2))
        else:   
            message = jsonify({"success": False, "message": "Failed to update new to balance!"})
            # amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="swap.error", body=message, properties=pika.BasicProperties(delivery_mode = 2))

    # Returns new and old wallet balance for to and from currency
    response = {
            "old " + from_currency : old_from_balance,
            "old " + to_currency : old_to_balance,
            "updated " + from_currency : updated_from_balance,
            "updated " + to_currency : updated_to_balance,
        }
    return response

def getNumber(amount_owned,coin):
    amount_owned = amount_owned[coin]
    return amount_owned

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__))
    app.run(host="0.0.0.0", port=5004, debug=True)
