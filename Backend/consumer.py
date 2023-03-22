from kafka import KafkaConsumer


TOPIC_NAME = 'orders'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=['localhost:9092'], api_version=(0,11,5))

for message in consumer:
    print(message)