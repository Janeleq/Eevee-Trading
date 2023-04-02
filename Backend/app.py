import os
import socket 
import requests
import json
from invokes import invoke_http
from flask import Flask, redirect, render_template, url_for, request, jsonify
from flask_cors import CORS
import stripe
# from invokes import invoke_http

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')
CORS(app)

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
    return redirect("http://127.0.0.1:5010/BNB")

#BITCOIN
@app.route("/BTC")
def bitcoin():
    return redirect("http://127.0.0.1:5010/BTC")

#CARDANO
@app.route("/ADA")
def cardano():
    return redirect("http://127.0.0.1:5010/ADA")

#DOGE
@app.route("/DOGE")
def doge():
    return redirect("http://127.0.0.1:5010/DOGE")

#ETHEREUM
@app.route("/ETH")
def ethereum():
    return redirect("http://127.0.0.1:5010/ETH")

# SOLANA
@app.route("/SOL")
def solana():
    return redirect("http://127.0.0.1:5010/SOL")

@app.route('/topup', methods=['GET', 'POST'])
def topup():
    topUpURL = 'http://localhost:5005/processtopup'
    print("\n--- Invoking Topup Microservice ---")
    return redirect(topUpURL)


@app.route('/thanks')
def processTopUp():
    top_up_amt = request.args.get('top_up_amt')
    transaction_id = request.args.get('transaction_id')
    status = request.args.get('status')
    
    # top_up_amt is preset to 1 and stripe ensure no -ve numbers can be entered, so there wont be any human errors
    if top_up_amt != 0:
        status = 200
        print('Top Up Amount: ', top_up_amt)
        return render_template('thanks.html', top_up_amt=top_up_amt, status=status, transaction_id=transaction_id)
    else:
        status = 'Error! Try topping up again!'
        profile_page_URL = "http://localhost:5000/profile"
        return redirect(profile_page_URL)

    


if __name__ == '__main__':
    app.run(port=5000, debug=True)