# make_transaction complex Microservice
# have to invoke wallet.py to check wheter got enough $$ to eg buy cc defined

from flask import Flask, redirect, render_template, url_for, request
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http

import pika
import json

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')
CORS(app)

#set up RabbitMQ Connection
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.queue_declare(queue='buy_order_queue')
marketplace_URL = "http://localhost:5000/marketplace"
price_URL =  "http://127.0.0.1:5001" 
# buy_transaction_URL =  "http://localhost:5004/" 
# sell_transaction_URL =  "http://localhost:5004/" 

def getQty(qty):
    return qty


def getPrice(response):
    price = response['data']['price']
    price = str(price)
    return price


@app.route("/<string:coin>/buy")
def buycc(coin):
    qty = request.args.get('buyqty')
    getQty(qty)
    price_URL = "http://localhost:5001" 
    price_URL = price_URL + "/coin/" + coin
    print(price_URL)
    response = requests.get(price_URL, timeout=10)
    print(response)
    status = '\n --- Invoking transaction microservice to settle Binance buy order ---'
    
    if response:
        response = response.json()
        price = getPrice(response)
        total_amount = round(float(qty) * float(price),2)
        #access wallet total usd balance
        #if wallet balance >= total_amount: carry on
        #else error
        return str(total_amount)
    else:
        return("Hello World")
    
@app.route("/<string:coin>/sell")
def sellcc(coin):
    qty = request.args.get('sellqty')
    getQty(qty)
    price_URL = "http://localhost:5001" 
    price_URL = price_URL + "/coin/" + coin
    print(price_URL)
    response = requests.get(price_URL, timeout=10)
    print(response)
    status = '\n --- Invoking transaction microservice to settle Binance buy order ---'
    # access wallet qty of coin 
    #if qty of coin in wallet >= sold: carry out transaction
    #else: error
    if response:
        response = response.json()
        price = getPrice(response)
        total_amount = round(float(qty) * float(price),2)
        #update wallet + cryptocurrency owned
        return str(total_amount)

    else:
        return("Hello World")
    
@app.route("/<string:coin>/buyorder")
def buyordercc(coin):
    qty = request.args.get('buyorderqty')
    boprice = request.args.get('buyorderprice')
    price_URL = "http://localhost:5001" 
    price_URL = price_URL + "/coin/" + coin
    response = requests.get(price_URL, timeout=10)
    if response:
        response = response.json()
        current_price = getPrice(response)
        total_amount = round(float(qty) * float(boprice),2)
        #if total_amount <= wallet balance --> place buy order
        #else --> error
        #update wallet + cryptocurrency owned

        return str(total_amount)

    else:
        return 0 


@app.route("/<string:coin>/sellorder")
def sellordercc(coin):
    qty = request.args.get('sellorderqty')
    soprice = request.args.get('sellorderprice')
    price_URL = "http://localhost:5001" 
    price_URL = price_URL + "/coin/" + coin
    response = requests.get(price_URL, timeout=10)
    if response:
        response = response.json()
        current_price = getPrice(response)
        total_amount = round(float(qty) * float(current_price),2)
        #if qty sold <= qty owned --> place sell order
        #else --> error
        #update wallet + cryptocurrency owned

        return str(total_amount)

    else:
        return 0 


if __name__ == '__main__':
    app.run(port=5003, debug=True)









