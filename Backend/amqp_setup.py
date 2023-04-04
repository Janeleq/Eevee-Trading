RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'


import pika
from os import environ ###

#local RABBITMQ
hostname = environ.get('rabbit_host') or 'host.docker.internal'
port = environ.get('rabbit_port') or 5672
# connect to the broker and set up a communication channel in the connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='host.docker.internal'))

#################
channel = connection.channel()
#==================================================== Buy Order ========================================================================================================

exchangetype="fanout"
exchangename = 'buyorders'
RABBITMQ_BUY_QUEUE = 'buyordersqueue'
channel.exchange_declare(exchangename=exchangename, exchange_type=exchangetype, durable=True)
channel.queue_bind(exchange = exchangename, queue=RABBITMQ_BUY_QUEUE) 

    
#====================================================End Buy Order ========================================================================================================
#==================================================== Sell Order ========================================================================================================

exchangetype="fanout"
exchangename = 'sellorders'
RABBITMQ_SELL_QUEUE = 'sellordersqueue'
channel.exchange_declare(exchange= exchangename, exchange_type=exchangetype, durable=True)
    # 'durable' makes the queue survive broker restarts
channel.queue_bind(exchange = exchangename, queue=RABBITMQ_SELL_QUEUE) 

    
#==================================================== End Sell Order ========================================================================================================

"""
This function in this module sets up a connection and a channel to a cloud AMQP broker,
and declares a 'topic' exchange to be used by the microservices in the solution.
"""


def check_setup():
    # The shared connection and channel created when the module is imported may be expired, 
    # timed out, disconnected by the broker or a client;
    # - re-establish the connection/channel is they have been closed
    global connection, channel, hostname, port, exchangename, exchangetype

    if not is_connection_open(connection):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port, heartbeat=3600, blocked_connection_timeout=3600))
    if channel.is_closed:
        channel = connection.channel()
        channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)


def is_connection_open(connection):
    # For a BlockingConnection in AMQP clients,
    # when an exception happens when an action is performed,
    # it likely indicates a broken connection.
    # So, the code below actively calls a method in the 'connection' to check if an exception happens
    try:
        connection.process_data_events()
        return True
    except pika.exceptions.AMQPError as e:
        print("AMQP Error:", e)
        print("...creating a new connection.")
        return False