from confluent_kafka import admin, Producer, Consumer
import logging
import io

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s.%(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


# Consuming side
CONSUMER_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'testo',
    'auto.offset.reset': 'earliest',
}
consumer = Consumer(CONSUMER_CONFIG)
last_topic = list_topics(consumer)
logging.info(f"Subscribed to {last_topic}")
consumer.subscribe([last_topic])

# Producing side
KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092"
}
client = admin.AdminClient(KAFKA_CONFIG)
producer = Producer(KAFKA_CONFIG)

# Definitions
def list_topics(c: Consumer, filter_by="ztf"):
    topics = c.list_topics().topics.keys()
    return list(filter(lambda x: filter_by in x, list(topics)))[-1]


def to_stream_client(msg):
    topic_name = "MgC - " + msg
    new_topic = admin.NewTopic(topic_name, 1, 1)
    client.create_topics([new_topic])
    logging.info(f"Creating topic {topic_name}")
    to_stream_produce(msg, topic_name)


def to_stream_produce(msg, topic_name):
    try:
        logging.info(f"Producing {msg.value().decode(encoding='UTF-8')}")
        time.sleep(5)
        producer.produce(topic, value=bytes(msg, "utf-8"))
        producer.flush()
    except Exception as e:
        logging.error(f"Problem {e} with {msg}")


# Main
while True:
    msg = consumer.poll(timeout=10)  # Previously=120
    if msg:
        # data = get_message(msg)
        logging.info(f"Consuming {msg.value().decode(encoding='UTF-8')}")

        # Do something with data
        # Post data to new topic called MgC
        to_stream_client(msg)

    else:
        last_topic = list_topics(consumer)
        consumer.subscribe([last_topic])
