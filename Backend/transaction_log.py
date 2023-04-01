#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import json
import os

import amqp_setup

monitorBindingKey='#'

def receiveTransactionLog():
    amqp_setup.check_setup()
        
    queue_name = 'Transaction_Log'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

# Track Transactions that happened (Buy/Sell + Topping Up  + Swap transactions)
def processBuyLog(order):
    print("Recording an Buy log:")
    print(order)

def processSellLog(order):
    print("Recording an Sell log:")
    print(order)

def processSwapLog(order):
    print("Recording an Swap log:")
    print(order)

def processTopUpLog(order):
    print("Recording an order log:")
    print(order)

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveOrderLog()


#    print(price)
#     # url = "https://min-api.cryptocompare.com/data/price"

#     # parameters = {
#     #     "fsym": coin
#     # }

#     response = requests.post(url, params = parameters)

#     if response.status_code == 200:
#         result = response.json()
#         price = result['USD']
#         total_price = price * quantity
#         return ("Hi")
#         #invoke wallet microservice, if total_price > money in wallet --> give error --> update error log(?)
#         #else, update wallet balance, add to transactions log

# @app.route("/sell", methods=['POST'])
# def sellcc(coin, quantity):
#     #invoke pricing microservice
#     url = "https://min-api.cryptocompare.com/data/price"

#     parameters = {
#         "fsym": coin
#     }

#     response = requests.post(url, params = parameters)

#     if response.status_code == 200:
#         return ("Hi")
#     if response.status_code == 200:
#         result = response.json()
#         price = result['USD']
#         total_price = price * quantity
#         #invoke wallet microservice, if quantity sold > quantity owned --> give error --> update error log(?)
#         #else, update wallet balance, add to transactions log

# @app.route("/buyorder", methods=['POST'])
# def buyorder(coin, quantity, set_buy_price):

#     max_price = quantity * set_buy_price
#     #if max_price > wallet balance --> error
#     #else baam set
    

#     #need to keep retrieving data of pricing of the coin
#     unit_price = 0
#     #once coin price lower then set_buy_price --> undergo transaction and update wallet (update transaction log)(sale is based on the price at that tick of time)

    
#     # message = f'Buy order executed for {coin} at {unit_price} USD'
#     # channel.basic_publish(exchange='', routing_key='buy_order_queue', body=message)
#     # print(f'Sent message: {message}')
#     return("Hello World")

# @app.route("/sellorder", methods=['POST'])
# def sellorder(coin, quantity, set_sell_price):
#     #if quantity intended to sell > quantity owned --> error
#     #else baam set

#     #need to keep retrieving data of pricing of the coin
#     # unit_price = 0
#     # #once coin price higher then set_sell_price --> undergo transaction and update wallet (update transaction log) (sale is based on the price at that tick of time)

#     # if unit_price > set_sell_price:
#     #     return
#     # if response.status_code == 200:
#     #     return ("Hi")

#     # message = f'Sell order executed for {coin} at {unit_price} USD'
#     # channel.basic_publish(exchange='', routing_key='buy_order_queue', body=message)
#     # print(f'Sent message: {message}')
#     return("Hello World")


# def transactbuy():
#     return

# def transactsell():
#     return
if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveTransactionLog()
