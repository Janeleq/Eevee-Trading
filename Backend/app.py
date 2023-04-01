import os
import socket 
import requests
import json
from invokes import invoke_http
from flask import Flask, redirect, render_template, url_for, request
from flask_cors import CORS
import stripe
# from invokes import invoke_http

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')


# function to fetch hostname and ip to check different instances currently running 
def fetchDetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname) , str(host_ip)

def getPrice(response):
    price = response['data']['price']
    price = str(price)
    return price

# endpoints
@app.route("/")
def main():
    hostname, host_ip = fetchDetails()
    print(hostname, host_ip)
    return render_template('starterpage.html', HOSTNAME=hostname, IP=host_ip)

@app.route("/login")
def login():
    hostname, host_ip = fetchDetails()
    print(hostname, host_ip)
    return render_template('Login+Register Page/Login.html', HOSTNAME=hostname, IP=host_ip)

@app.route("/register")
def register():
    hostname, host_ip = fetchDetails()
    print(hostname, host_ip)
    return render_template('Register.html', HOSTNAME=hostname, IP=host_ip)

@app.route("/home")
def home():
    return render_template('homepageWithLogin/homepageWithLogin.html')

@app.route("/profile")
def profile():
    return render_template('coins/profilepage.html')


@app.route("/marketplace")
def marketplace():
    status = '\n --- Invoking pricing microservice to display various CC prices ---'
    print(status)
    return render_template('coins/marketplace.html', data = status)

@app.route("/swap")
def swap():
    hostname, host_ip = fetchDetails()
    return render_template('Swap.html', HOSTNAME=hostname, IP=host_ip)

# #BINANCE
@app.route("/BNB")
def binance():
    return render_template('coins/bnb.html')

def getQty(qty):
    return qty


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

# @app.route("/SOL/buy")
# def buySolana():
#     status = '\n --- Invoking transaction microservice to settle Solana buy order ---'
#     return status
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# @app.route("/SOL/sell")
# def sellSolana():
#     status = '\n --- Invoking transaction microservice to settle Solana sell order ---'
#     return(status)
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

topUpURL = 'http://localhost:5005/processtopup'
@app.route('/topup')
def topup():
    print("\n--- Invoking Topup Microservice ---")
    response = requests.get(topUpURL)
    if response:
        return 'Hi'
    else:
        return 'Bye'

if __name__ == '__main__':
    app.run(port=5000, debug=True)