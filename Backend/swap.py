from invokes import invoke_http
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/swap", methods = ['GET', 'POST'])
def swap(from_amount, from_currency, to_currency):
    # if request.method == 'GET':
    #     from_amount = request.form.get('from_amount')
    #     from_currency = request.form.get("from_currency")
    #     to_currency = request.form.get("to_currency")

    to_price_URL = ""
    from_price_URL = ""

    wallet_URL = ""
    conversion_ratio = getRatio(from_currency, to_currency)
    to_price_data = invoke_http(to_price_URL, 'GET')
    from_price_data = invoke_http(from_price_URL, 'GET')

    from_price = to_price_data['from_currency']
    to_price = from_price_data['to_currency']

    #Retrieves wallet balance 
    wallet_data = invoke_http(wallet_URL, 'GET', json=EMAIL)

    conversion_amount = from_amount * conversion_ratio

    #Updates wallet


    #Status of failed swap
    if <> not in range(200, 300):
        #AMQP activity
        
        return {
            "code": 500,
            "message": "Swap failure sent for error handling."
        }

    #Status of successful swap
    else:
        #AMQP activity

        return {
            "code": 400,
            'conversion_amount': conversion_amount
        }
    
def getConvertedAmount(conversion_amount):
    return {
        "amount" : conversion_amount
    }

#Obtain rates from price.py and calculates ratio of swap (to rate / from rate)
def getRatio(origin, target):
    origin_price = invoke_http(price_URL, method='GET', json=(origin))
    target_price = invoke_http(price_URL, method='GET', json=(target))
    return (origin / target)

#Update wallet of new balance
def updateWallet(walletId):
    pass 
