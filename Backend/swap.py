from invokes import invoke_http
from flask import Flask, request

price_URL = ""
wallet_URL = ""

@app.route("/swap", methods = ['GET', 'POST'])
def swap():
    if request.method == 'GET':
        from_amount = request.form.get('from_amount')
        from_currency = request.form.get("from_currency")
        to_currency = request.form.get("to_currency")
    
    conversion_ratio = getRatio(from_currency, to_currency)
    price_data = invoke_http(price_URL, 'GET')
    from_price = price_data['from_currency']
    to_price = price_data['to_currency']

    #Retrieves wallet balance 
    wallet_data = invoke_http(wallet_URL, 'GET')

    conversion_amount = from_amount * conversion_ratio

    #Updates wallet

    #Status of failed swap
    if code not in range(200, 300):
        #AMQP activity

        return {
            "code": 500,
            "message": "Swap failure sent for error handling."
        }

    #Status of successful swap
    else:
        #AMQP activity
        return {
            "code": 400,
            'conversion_amount': conversion_amount
        }
    
#Obtain rates from price.py and calculates ratio of swap (to rate / from rate)
def getRatio(origin, target):
    origin_price = invoke_http(price_URL, method='GET', json=(origin))
    target_price = invoke_http(price_URL, method='GET', json=(target))
    return (origin / target)

#Update wallet of new balance
def updateWallet(walletId):
    pass 
