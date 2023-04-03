# make_transaction complex Microservice
# have to invoke wallet.py to check wheter got enough $$ to eg buy cc defined

from flask import Flask, redirect, render_template, url_for, request, jsonify
from flask_cors import CORS
import time
import pyrebase
import os, sys
from os import environ
import helpers
import requests
from invokes import invoke_http

import pika
import json

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')
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


#set up RabbitMQ Connection
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.queue_declare(queue='buy_order_queue')
marketplace_URL = "http://localhost:5000/marketplace"
price_URL = "http://127.0.0.1:5001" 
# buy_transaction_URL = "http://localhost:5004/" 
# sell_transaction_URL = "http://localhost:5004/" 



def dummy(qty):
    return float(qty)

def getPrice(response):
    price = response['data']['price']
    price = str(price)
    return price

def getNumber(number,coin):
    # number = number[coin]
    return number

# #BINANCE
@app.route("/BNB")
def binance():
    return render_template('coins/bnb.html')

#BITCOIN
@app.route("/BTC")
def bitcoin():
    return render_template('coins/btc.html')

#CARDANO
@app.route("/ADA")
def cardano():
    return render_template('coins/ada.html')

#DOGE
@app.route("/DOGE")
def doge():
    return render_template('coins/doge.html')

#ETHEREUM
@app.route("/ETH")
def ethereum():
    return render_template('coins/eth.html')

# SOLANA
@app.route("/SOL")
def solana():
    return render_template('coins/sol.html')


@app.route("/<string:coin>/buy")
def buycc(coin):
    qty = request.args.get('buyqty')
    qty = dummy(qty)
    price_URL = "http://localhost:5001" 
    price_URL = price_URL + "/coin/" + coin
    wallet_USD = "http://localhost:5100/wallet/USD"
    wallet_URL = "http://localhost:5100/wallet/" + coin
    #get price
    response = requests.get(price_URL, timeout=10)
    #get USD owned
    amount_owned = requests.get(wallet_USD, timeout=10)
    
    if response:
        #get total price needed to pay with current price + quantity
        response = response.json()
        price = getPrice(response)
        total_amount = round(float(qty) * float(price),2)

    if amount_owned:
        amount_owned = amount_owned.json()
        qty_usd_owned = getNumber(amount_owned, "USD")

    if qty_usd_owned >= total_amount:
        qty_coin_owned = requests.get(wallet_URL)
        if qty_coin_owned:
            # id = 'DsU3Gmoe1McjyXU8JA66GfiBG7L2'
            id = helpers.retrieveHelperVal('uID','helpers.txt')
            ownedcoin = qty_coin_owned.json()
            ownedcoin = getNumber(ownedcoin, coin)
            decrease = qty_usd_owned - total_amount
            increase = float(ownedcoin) + float(qty)
            database.child("users").child(id).child('wallet_coins').child("USD").update({"qty":decrease})
            database.child("users").child(id).child('wallet_coins').child(coin).update({"qty": increase})
            result = {
                "code":200,
                "message": "Transaction successful!"
            }, 200
            return result
        else:
            return "haha"
    else:
        result = {
            "code" : 400,
            "message": "Transaction failed, please try again as you do not have enough balance in your wallet to make the transaction."
        }, 400
        return result 
    

@app.route("/<string:coin>/sell")
def sellcc(coin):
    qty = request.args.get('sellqty')
    qty = dummy(qty)
    price_URL = "http://localhost:5001" 
    price_URL = price_URL + "/coin/" + coin
    wallet_USD = "http://localhost:5100/wallet/USD"
    wallet_URL = "http://localhost:5100/wallet/" + coin
    #get price
    response = requests.get(price_URL, timeout=10)
    coin_owned = requests.get(wallet_URL)

    if coin_owned:
        coin_owned = coin_owned.json()
        qty_coin_owned = getNumber(coin_owned, coin)

    if response:
        #get total price needed to pay with current price + quantity
        response = response.json()
        price = getPrice(response)
        total_amount = round(float(qty) * float(price),2)

    if qty_coin_owned >= float(qty):
        amount_owned = requests.get(wallet_USD)
        if amount_owned:
            id = helpers.retrieveHelperVal('uID','helpers.txt')
            qty_usd_owned = amount_owned.json()
            qty_usd_owned = getNumber(qty_usd_owned, "USD")
            decrease = float(qty_coin_owned) - float(qty)
            increase = qty_usd_owned + total_amount
            database.child("users").child(id).child('wallet_coins').child("USD").update({"qty":increase})
            database.child("users").child(id).child('wallet_coins').child(coin).update({"qty": decrease})
            result = {
                "code":200,
                "message": "Transaction successful!"
            }, 200
            return result
        else:
            return "haha"
    else:
        result = {
            "code" : 400,
            "message": "Transaction failed, please try again as you do not have enough balance in your wallet to make the transaction."
        }, 400
        return result 


@app.route("/<string:coin>/buyorder")
def buyordercc(coin):
    boqty = request.args.get('buyorderqty')
    boqty = dummy(boqty)
    boprice = request.args.get('buyorderprice')
    boprice = dummy(boprice)
    wallet_USD = "http://localhost:5100/wallet/USD"
    wallet_URL = "http://localhost:5100/wallet/" + coin

    price_URL = "http://localhost:5001" 
    price_URL = price_URL + "/coin/" + coin
    response = requests.get(price_URL, timeout=10)
    #1. get total amount needed
    total_amount_needed = float(boqty) * float(boprice)
    #2. get wallet balance in USD
    total_usd_owned = requests.get(wallet_USD, timeout=10)
    #3. compare --> if wallet balance >= total amount --> place in order/ create order details
    if total_usd_owned:
        total_usd_owned = total_usd_owned.json()
        total_usd_owned = getNumber(total_usd_owned, "USD")
    if total_usd_owned >= total_amount_needed:
        #place order
        order_details = {
            'total_amount_required' : total_amount_needed,
            'buy_quantity': boqty,
            'buy_price': boprice,
            'orderid': 2
        }
        database.child('users').child(id).child('orders').push({"order{order_details['orderid']}":{'orderid':order_details['orderid'], 'details': order_details}})
    #4. AMQP stuff

    if response:
        #get total price needed to pay with current price + quantity
        response = response.json()
        price = getPrice(response)
        
    if amount_owned:
        amount_owned = amount_owned.json()
        qty_usd_owned = getNumber(amount_owned, "USD")


        #if total_amount <= wallet balance --> place buy order and create id (ascending order) 
        #else --> error
        #update wallet + cryptocurrency owned
        return

    else:
        return 0 
# while True:
#     check_order()
#     time.sleep(10)
    
def check_order(orderid):
    return



@app.route("/<string:coin>/sellorder")
def sellordercc(coin):
    soqty = request.args.get('sellorderqty')
    soqty = dummy(soqty)
    soprice = request.args.get('sellorderprice')
    soprice = dummy(soprice)
    wallet_USD = "http://localhost:5100/wallet/USD"
    wallet_URL = "http://localhost:5100/wallet/" + coin

    price_URL = "http://localhost:5001" 
    price_URL = price_URL + "/coin/" + coin
    response = requests.get(price_URL, timeout=10)
    #get USD owned

    #1. get qty to sell

    #2. get qty owned

    #3. compare --> if qty owned >= qty sold --> place in order/ create order details

    #4. AMQP stuff


if __name__ == '__main__':
    app.run(port=5010, debug=True)









