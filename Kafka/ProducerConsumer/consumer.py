from confluent_kafka import Consumer
import fastavro
import logging
import io

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s.%(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

CONSUMER_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'testo',
    'auto.offset.reset': 'earliest',
}


def list_topics(c: Consumer, filter_by="ztf"):
    topics = c.list_topics().topics.keys()
    return list(filter(lambda x: filter_by in x, list(topics)))[-1]


def get_message(message):
    bytes_io = io.BytesIO(message.value())
    reader = fastavro.reader(bytes_io)
    return reader.next()


consumer = Consumer(CONSUMER_CONFIG)
last_topic = list_topics(consumer)
logging.info(f"Subscribed to {last_topic}")
consumer.subscribe([last_topic])

while True:
    msg = consumer.poll(timeout=120)
    if msg:
        # data = get_message(msg)
        logging.info(f"Consuming {msg.value()}")
        # Do something with data
    else:
        last_topic = list_topics(consumer)
        consumer.subscribe([last_topic])