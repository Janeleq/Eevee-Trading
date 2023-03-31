import os
import socket 
import requests
from invokes import invoke_http
from flask import Flask, redirect, render_template, url_for, request
from flask_cors import CORS
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

@app.route("/BNB/buy")
def buyBinance():
    price_URL = "http://localhost:5001" 
    price_URL = price_URL + "/" + 'BNB' + "/price"
    response = invoke_http(price_URL)
    print(response)
    status = '\n --- Invoking transaction microservice to settle Binance buy order ---'
    return response
    return("Hello World")
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

@app.route("/BNB/sell")
def sellBinance():
    price_URL = "http://localhost:5001" 
    status = '\n --- Invoking transaction microservice to settle Binance sell order ---'
    return(status)
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)
    
#BITCOIN
@app.route("/BTC")
def bitcoin():
    return render_template('coins/btc.html')

@app.route("/BTC/buy")
def buyBitcoin():
    status = '\n --- Invoking transaction microservice to settle Bitcoin buy order ---'
    return status
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

@app.route("/BTC/sell")
def sellBitcoin():
    status = '\n --- Invoking transaction microservice to settle Bitcoin sell order ---'
    return(status)
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

#CARDANO
@app.route("/ADA")
def cardano():
    return render_template('coins/ada.html')

@app.route("/ADA/buy")
# def buyCardano():
#     status = '\n --- Invoking transaction microservice to settle Cardano buy order ---'
#     print(status)
#     price = invoke_http('localhost:5003/price', 'GET')
#     print(price)
#     return status
    # return status
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

@app.route("/ADA/sell")
def sellCardano():
    status = '\n --- Invoking transaction microservice to settle Cardano sell order ---'
    return(status)
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

#DOGE
@app.route("/DOGE")
def doge():
    return render_template('coins/doge.html')

@app.route("/DOGE/buy")
def buyDoge():
    status = '\n --- Invoking transaction microservice to settle DOGE buy order ---'
    return status
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

@app.route("/DOGE/sell")
def sellDoge():
    status = '\n --- Invoking transaction microservice to settle DOGE sell order ---'
    return(status)
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

#ETHEREUM
@app.route("/ETH")
def ethereum():
    return render_template('coins/eth.html')

@app.route("/ETH/buy")
def buyEth():
    status = '\n --- Invoking transaction microservice to settle Ethereum buy order ---'
    return status
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

@app.route("/ETH/sell")
def sellEth():
    status = '\n --- Invoking transaction microservice to settle Ethereum sell order ---'
    return(status)
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

# SOLANA
@app.route("/SOL")
def solana():
    return render_template('coins/sol.html')

@app.route("/SOL/buy")
def buySolana():
    status = '\n --- Invoking transaction microservice to settle Solana buy order ---'
    return status
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

@app.route("/SOL/sell")
def sellSolana():
    status = '\n --- Invoking transaction microservice to settle Solana sell order ---'
    return(status)
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

@app.route("/topup")
def topUpWallet():
    status = '\n --- Bringing you to top-up page ---'
    return redirect("https://buy.stripe.com/test_00g5nJ2nW3GC1zO288")
    # result = invoke_http("http:localhost:5000/transaction", method='POST')
    # print(result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)