from kafka import KafkaProducer


TOPIC_NAME = 'orders'
KAFKA_SERVER = 'localhost:9092'


producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, api_version=(0,11,5))

producer.send(TOPIC_NAME, b'TEST MESSAGE!!!')
producer.flush()
producer.send('foobar', key=b'foo', value=b'bar')