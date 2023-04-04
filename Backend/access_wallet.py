# Complex Wallet Microservice
from flask import Flask, render_template, session, request, redirect,url_for,flash,current_app,make_response, jsonify
from flask_cors import CORS
import pyrebase 
import helpers

app = Flask(__name__)
CORS(app)

#Firebase configurations
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
#Initialize firebase
fb = pyrebase.initialize_app(firebase_config)
database = fb.database()

#access wallet details to return currency owned in JSON
@app.route("/wallet")
def retrieveWallet():
    id = helpers.retrieveHelperVal('uID','helpers.txt')
    userdetails = database.child("users").child(id).get()
    wallet_coins = userdetails.val()['wallet_coins']
    currencyowned = {
        "BNB": wallet_coins['BNB']['qty'],
        "BTC": wallet_coins['BTC']['qty'],
        "ADA": wallet_coins['ADA']['qty'],
        "DOGE": wallet_coins['DOGE']['qty'],
        "ETH": wallet_coins['ETH']['qty'],
        "SOL": wallet_coins['SOL']['qty'],
        "USD": wallet_coins['USD']['qty'],
    }
    return currencyowned

#access wallet details to return specific currency owned
@app.route("/wallet/<string:coin>")
def retrieveCurrency(coin):
    id = helpers.retrieveHelperVal('uID','helpers.txt')
    userdetails = database.child("users").child(id).get()
    wallet_coins = userdetails.val()['wallet_coins']
    return str((wallet_coins[coin]['qty']))

#shows profile page
@app.route('/profile')
def profile():
    return render_template('coins/profilepage.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=True)