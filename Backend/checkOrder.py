from flask import Flask
from flask_cors import CORS
import pika
import json
import pyrebase
import os
import helpers
import requests
import threading


app = Flask(__name__)
CORS(app)

RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'
RABBITMQ_EXCHANGE = 'buyorders'
RABBITMQ_QUEUE = 'buyordersqueue'





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
def dummy(lel):
    price = lel.json()['data']['price']
    return float(price)

def checkBuyOrderStatus():
    threading.Timer(5.0, checkBuyOrderStatus).start()
    if os.path.exists('helpers.txt')==True:
        id = helpers.retrieveHelperVal('uID','helpers.txt')
        orderlist = database.child('users').child(id).child('buyorders').get()
        print(orderlist.val())
        if orderlist.val() == None:
            pass
        else:
            for order in orderlist:
                order = order.val()
                coin_of_interest = order['ordercoin']
                current_coin_pricing = requests.get('http://localhost:5001/coin/' + coin_of_interest)
                if current_coin_pricing:
                    current_coin_pricing = dummy(current_coin_pricing)
                    if current_coin_pricing <= order['buy_price']:
                        buy=requests.get('http://localhost:5010/'+ coin_of_interest + '/buy?buyqty=' + str(order['buy_quantity']))
                        database.child('users').child(id).child('buyorders').remove(coin_of_interest)
                        if buy:
                            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)))
                            channel = connection.channel()

                            # Declare exchange and queue
                            channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='fanout')
                            channel.queue_declare(queue=RABBITMQ_QUEUE)
                            channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=RABBITMQ_QUEUE)
                            # Publish order to exchange
                            # order = {'symbol': data['symbol'], 'amount': data['amount'], 'price': data['price'], 'total_value': total_value}
                            # channel.basic_publish(exchange=RABBITMQ_EXCHANGE, routing_key='', body=json.dumps(order))

                            # Close RabbitMQ connection
                            connection.close()
                            print('donezbuyer')
                    else:
                        pass
                else:
                    pass



def checkSellOrderStatus():
    threading.Timer(5.0, checkSellOrderStatus).start()
    if os.path.exists('helpers.txt')==True:
        id = helpers.retrieveHelperVal('uID','helpers.txt')
        orderlist = database.child('users').child(id).child('sellorders').get()
        print(orderlist.val())
        if orderlist.val() == None:
            print('loserseller')
            pass
        else:
            for order in orderlist:
                order = order.val()
                coin_of_interest = order['ordercoin']
                current_coin_pricing = requests.get('http://localhost:5001/coin/' + coin_of_interest)
                if current_coin_pricing:
                    current_coin_pricing = dummy(current_coin_pricing)
                    if current_coin_pricing >= order['sell_price']:
                        print('wassupseller')
                        sell=requests.get('http://localhost:5010/'+ coin_of_interest + '/sell?sellqty=' + str(order['sell_quantity']))
                        database.child('users').child(id).child('sellorders').remove(coin_of_interest)
                        if sell:
                            print('donezseller')
                    else:
                        pass
                else:
                    return 0

fb = pyrebase.initialize_app(firebase_config)
database = fb.database()
checkBuyOrderStatus()
checkSellOrderStatus()




if __name__ == '__main__':
    app.run(port=5200, debug=True)
