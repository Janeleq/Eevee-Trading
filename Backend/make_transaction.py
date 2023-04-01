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

def buycc(coin, qty):
    price_URL = price_URL + "/" + coin + "/price"
    response = requests.get(price_URL)
    
    buy_price = 0
    
    totalamount = buy_price * qty

    #retrieve wallet balance
    #if total amount more than wallet balance --> error
    #else: update wallet, update transaction log(?)
    

    return response.json()

def sellcc(coin, qty):
    price_URL = price_URL + "/" +coin + "/price"
    response = requests.get(price_URL)
    sell_price = 0

    #if qty sold > qty owned --> error
    #else:
    totalamount = sell_price * qty
    #update wallet, transaction log

    return response.json()


def buyordercc(coin, qty, boprice):
    price_URL = price_URL + "/" +coin + "/price"
    response = requests.get(price_URL)
    
    #get buy price

    #get wallet balance

    total_amount = boprice * qty

    #if total_amount > wallet balance --> error
    #else: placed order --> message queue
        #if boprice < buy_price:
        #carry on with transaction, update wallet and transaction log
        #else pass
    return response.json()

def sellordercc(coin, qty, soprice):
    price_URL = price_URL + "/" +coin + "/price"
    response = requests.get(price_URL)

     #get sell price

    #get wallet balance

    #if qty sold > qty owned --> error


    #else: placed order --> message queue
        #total_amount = soprice * qty
        #if soprice > sell_price:
        #carry on with transaction, update wallet and transaction log
        #else pass
        
    return response.json()



if __name__ == '__main__':
    app.run(port=5003, debug=True)












# #BINANCE
# @app.route("/BNB")
# def binance():
#     return render_template('coins/bnb.html')

# @app.route("/BNB/buy")
# def buyBinance():

#     status = '\n --- Invoking transaction microservice to settle Binance buy order ---'
#     print(status)
#     price = invoke_http(price_URL, 'GET', json=None)
#     print(price)

#     return status
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# @app.route("/BNB/sell")
# def sellBinance():
#     status = '\n --- Invoking transaction microservice to settle Binance sell order ---'
#     print(status)
#     return(status)
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)
    
# #BITCOIN
# @app.route("/BTC")
# def bitcoin():
#     return render_template('coins/btc.html')

# @app.route("/BTC/buy")
# def buyBitcoin():
#     status = '\n --- Invoking transaction microservice to settle Bitcoin buy order ---'
#     print(status)
    
#     return status
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# @app.route("/BTC/sell")
# def sellBitcoin():
#     status = '\n --- Invoking transaction microservice to settle Bitcoin sell order ---'
#     print(status)
#     return(status)
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# #CARDANO
# @app.route("/ADA")
# def cardano():
#     return render_template('coins/ada.html')

# @app.route("/ADA/buy")
# def buyCardano():
#     status = '\n --- Invoking transaction microservice to settle Cardano buy order ---'
#     print(status)
#     price = invoke_http('localhost:5003/price', 'GET')
#     print(price)
#     # return 1
#     # return status
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# @app.route("/ADA/sell")
# def sellCardano():
#     status = '\n --- Invoking transaction microservice to settle Cardano sell order ---'
#     print(status)
#     return(status)
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# #DOGE
# @app.route("/DOGE")
# def doge():
#     return render_template('coins/doge.html')

# @app.route("/DOGE/buy")
# def buyDoge():
#     status = '\n --- Invoking transaction microservice to settle DOGE buy order ---'
#     print(status)
    
#     return status
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# @app.route("/DOGE/sell")
# def sellDoge():
#     status = '\n --- Invoking transaction microservice to settle DOGE sell order ---'
#     print(status)
#     return(status)
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# #ETHEREUM
# @app.route("/ETH")
# def ethereum():
#     return render_template('coins/eth.html')

# @app.route("/ETH/buy")
# def buyEth():
#     status = '\n --- Invoking transaction microservice to settle Ethereum buy order ---'
#     print(status)
    
#     return status
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# @app.route("/ETH/sell")
# def sellEth():
#     status = '\n --- Invoking transaction microservice to settle Ethereum sell order ---'
#     print(status)
#     return(status)
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# # SOLANA
# @app.route("/SOL")
# def solana():
#     return render_template('coins/sol.html')

# @app.route("/SOL/buy")
# def buySolana():
#     status = '\n --- Invoking transaction microservice to settle Solana buy order ---'
#     print(status)
    
#     return status
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# @app.route("/SOL/sell")
# def sellSolana():
#     status = '\n --- Invoking transaction microservice to settle Solana sell order ---'
#     print(status)
#     return(status)
#     # result = invoke_http("http:localhost:5000/transaction", method='POST')
#     # print(result)

# @app.route("/ADA/buy", methods=['POST'])
# def buyADA():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=ADA')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})

# @app.route("/BTC/buy", methods=['POST'])
# def buyBTC():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=BTC')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})

# @app.route("/BNB/buy", methods=['POST'])
# def buyBNB():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=BNB')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})

# @app.route("/DOGE/buy", methods=['POST'])
# def buyDOGE():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=DOGE')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})

# @app.route("/ETH/buy", methods=['POST'])
# def buyETH():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=ETH')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})

# @app.route("/SOL/buy", methods=['POST'])
# def buySOL():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=SOL')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})


#selling

# @app.route("/ADA/sell", methods=['POST'])
# def sellADA():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=ADA')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})

# @app.route("/BTC/sell", methods=['POST'])
# def sellBTC():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=BTC')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})

# @app.route("/BNB/sell", methods=['POST'])
# def sellBNB():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=BNB')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})

# @app.route("/DOGE/sell", methods=['POST'])
# def sellDOGE():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=DOGE')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})

# @app.route("/ETH/sell", methods=['POST'])
# def sellETH():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=ETH')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})

# @app.route("/SOL/sell", methods=['POST'])
# def sellSOL():
#     data = request.json
#     quantity = data.get('amount')

#     response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=SOL')
#     price = response.json()['USD']

#     total_cost = quantity * price
    
#     return jsonify({'total_cost': total_cost})



# # @app.route("/place_order", methods=['POST'])

# # def place_order():
# #     # Simple check of input format and data of the request are JSON
# #     if request.is_json:
# #         try:
# #             order = request.get_json()
# #             print("\nReceived an order in JSON:", order)

# #             # do the actual work
# #             # 1. Send order info {cart items}
# #             result = processPlaceOrder(order)
# #             print('\n------------------------')
# #             print('\nresult: ', result)
# #             return jsonify(result), result["code"]

# #         except Exception as e:
# #             # Unexpected error in code
# #             exc_type, exc_obj, exc_tb = sys.exc_info()
# #             fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
# #             ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
# #             print(ex_str)

# #             return jsonify({
# #                 "code": 500,
# #                 "message": "place_order.py internal error: " + ex_str
# #             }), 500

# #     # if reached here, not a JSON request.
# #     return jsonify({
# #         "code": 400,
# #         "message": "Invalid JSON input: " + str(request.get_data())
# #     }), 400


# # def processPlaceOrder(order):
# #     # 2. Send the order info {cart items}
# #     # Invoke the order microservice
# #     print('\n-----Invoking order microservice-----')
# #     order_result = invoke_http(order_URL, method='POST', json=order)
# #     print('order_result:', order_result)
  
# #     # Check the order result; if a failure, send it to the error microservice.
# #     code = order_result["code"]
# #     message = json.dumps(order_result)

# #     amqp_setup.check_setup()

# #     if code not in range(200, 300):
# #         # Inform the error microservice
# #         #print('\n\n-----Invoking error microservice as order fails-----')
# #         print('\n\n-----Publishing the (order error) message with routing_key=order.error-----')

# #         # invoke_http(error_URL, method="POST", json=order_result)
# #         amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order.error", 
# #             body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
# #         # make message persistent within the matching queues until it is received by some receiver 
# #         # (the matching queues have to exist and be durable and bound to the exchange)

# #         # - reply from the invocation is not used;
# #         # continue even if this invocation fails        
# #         print("\nOrder status ({:d}) published to the RabbitMQ Exchange:".format(
# #             code), order_result)

# #         # 7. Return error
# #         return {
# #             "code": 500,
# #             "data": {"order_result": order_result},
# #             "message": "Order creation failure sent for error handling."
# #         }

# #     # Notice that we are publishing to "Activity Log" only when there is no error in order creation.
# #     # In http version, we first invoked "Activity Log" and then checked for error.
# #     # Since the "Activity Log" binds to the queue using '#' => any routing_key would be matched 
# #     # and a message sent to “Error” queue can be received by “Activity Log” too.

# #     else:
# #         # 4. Record new order
# #         # record the activity log anyway
# #         #print('\n\n-----Invoking activity_log microservice-----')
# #         print('\n\n-----Publishing the (order info) message with routing_key=order.info-----')        

# #         # invoke_http(activity_log_URL, method="POST", json=order_result)            
# #         amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order.info", 
# #             body=message)
    
# #     print("\nOrder published to RabbitMQ Exchange.\n")
# #     # - reply from the invocation is not used;
# #     # continue even if this invocation fails
    
# #     # 5. Send new order to shipping
# #     # Invoke the shipping record microservice
# #     print('\n\n-----Invoking shipping_record microservice-----')    
    
# #     shipping_result = invoke_http(
# #         shipping_record_URL, method="POST", json=order_result['data'])
# #     print("shipping_result:", shipping_result, '\n')

# #     # Check the shipping result;
# #     # if a failure, send it to the error microservice.
# #     code = shipping_result["code"]
# #     if code not in range(200, 300):
# #         # Inform the error microservice
# #         #print('\n\n-----Invoking error microservice as shipping fails-----')
# #         print('\n\n-----Publishing the (shipping error) message with routing_key=shipping.error-----')

# #         # invoke_http(error_URL, method="POST", json=shipping_result)
# #         message = json.dumps(shipping_result)
# #         amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="shipping.error", 
# #             body=message, properties=pika.BasicProperties(delivery_mode = 2))

# #         print("\nShipping status ({:d}) published to the RabbitMQ Exchange:".format(
# #             code), shipping_result)

# #         # 7. Return error
# #         return {
# #             "code": 400,
# #             "data": {
# #                 "order_result": order_result,
# #                 "shipping_result": shipping_result
# #             },
# #             "message": "Simulated shipping record error sent for error handling."
# #         }

# #     # 7. Return created order, shipping record
# #     return {
# #         "code": 201,
# #         "data": {
# #             "order_result": order_result,
# #             "shipping_result": shipping_result
# #         }
# #     }


# # # Execute this program if it is run as a main script (not by 'import')
# # if __name__ == "__main__":
# #     print("This is flask " + os.path.basename(__file__) + " for placing an order...")
# #     app.run(host="0.0.0.0", port=5100, debug=True)
# #     # Notes for the parameters: 
# #     # - debug=True will reload the program automatically if a change is detected;
# #     #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
# #     # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
# #     #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
# #     #   -- as long as the hosts can already reach the machine running the flask program along the network;
# #     #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
