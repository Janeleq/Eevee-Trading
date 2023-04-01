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


@app.route('/topup', methods=['GET', 'POST'])
def topup():
    topUpURL = 'http://localhost:5005/processtopup'
    print("\n--- Invoking Topup Microservice ---")
    return redirect(topUpURL)
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)