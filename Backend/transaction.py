# Check Transactions that happened (Buy/Sell + Topping Up transactions)

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
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(port=5002, debug=True)
