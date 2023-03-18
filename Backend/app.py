import os
from flask import Flask, redirect, render_template, url_for


app = Flask(__name__, template_folder='../Frontend/templates')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/binance")
def binance():
    return render_template('coins/binance.html')

@app.route("/bitcoin")
def bitcoin():
    return render_template('coins/bitcoin.html')

@app.route("/cardano")
def cardano():
    return render_template('coins/cardano.html')

@app.route("/doge")
def doge():
    return render_template('coins/doge.html')

@app.route("/ethereum")
def ethereum():
    return render_template('coins/ethereum.html')

@app.route("/profile")
def profile():
    return render_template('coins/profilepage.html')


@app.route("/simulatorhome")
def simulator():
    return render_template('coins/simulatorhome.html')


@app.route("/solana")
def solanaa():
    return render_template('coins/solana.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)