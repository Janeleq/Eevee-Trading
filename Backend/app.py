import os
import socket 
from flask import Flask, redirect, render_template, url_for
from invokes import invoke_http

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
    return render_template('index.html', HOSTNAME=hostname, IP=host_ip)

@app.route("/login")
def login():
    return render_template('Login+Register Page/Login.html')

@app.route("/home")
def home():
    return render_template('homepageWithLogin/homepageWithLogin.html')

@app.route("/BNB")
def binance():
    return render_template('coins/bnb.html')

@app.route("/BTC")
def bitcoin():
    return render_template('coins/btc.html')

@app.route("/ADA")
def cardano():
    return render_template('coins/ada.html')

@app.route("/DOGE")
def doge():
    return render_template('coins/doge.html')

@app.route("/ETH")
def ethereum():
    return render_template('coins/eth.html')

@app.route("/profile")
def profile():
    return render_template('coins/profilepage.html')


@app.route("/simulator")
def simulator():
    return render_template('coins/simulatorhome.html')


@app.route("/SOL")
def solanaa():
    return render_template('coins/sol.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)