# Complex Wallet Microservice
from flask import Flask, render_template, session, request, redirect,url_for,flash,current_app,make_response
from flask_cors import CORS
import pyrebase
import stripe 

app = Flask(__name__)
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

firebase = pyrebase.initialize_app(firebase_config)
database = firebase.database




@app.route("/wallet/read")
def retrieveWallet():
    #do the read function
    return


@app.route("/wallet/update")
def updateWallet(coin1, coin2):
    return




@app.route('/profile')
def profile():
    return render_template('coins/profilepage.html')

# publishable_key = "pk_test_51Mqv3mL81p6Fg6ebcfrJYprowuiyEYky8iILawOUGwdd7WEjxkQk6hJRfSXm02XdbgzBU0qGmhJxoA737LI0mDcm004m87jVGX"
# stripe.api_key = "sk_test_51Mqv3mL81p6Fg6ebxNqIERpNmaW1FIyE0Ps6EH6A3UHKI9pMVIlUR6ExCmOwlrrBXArZPTLu0GnF8wOppX16g2qq00hB17R6OX"

# @app.route('/topup')
# def topUpWallet():
#     invoice = request.get('invoice')
#     amount = request.form.get('amount')

#     customer = stripe.Customer.create(
#       email=request.form['stripeEmail'],
#       source=request.form['stripeToken'],
#     )

#     charge = stripe.Charge.create(
#       customer=customer.id,
#       description='Myshop',
#       amount=amount,
#       currency='usd',
#     )

#     orders =  CustomerOrder.query.filter_by(customer_id = current_user.id,invoice=invoice).order_by(CustomerOrder.id.desc()).first()
#     orders.status = 'Paid'

#     return redirect(url_for('profile'))


if __name__ == '__main__':
    app.run(port=5100, debug=True)