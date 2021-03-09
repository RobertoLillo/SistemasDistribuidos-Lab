from confluent_kafka import admin, Producer, Consumer
import fastavro
import logging
import json
import time 
import io

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s.%(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def list_topics(c: Consumer, filter_by="ztf"):
    topics = c.list_topics().topics.keys()
    return list(filter(lambda x: filter_by in x, list(topics)))[-1]


def get_message(message):
    bytes_io = io.BytesIO(message.value())
    reader = fastavro.reader(bytes_io)
    return reader.next()


def to_stream_dir(kafka_client):
    topic_name = "MgC-Topic"
    new_topic = admin.NewTopic(topic_name, 1, 1)
    kafka_client.create_topics([new_topic])
    logging.info(f"Creating topic {topic_name}")
    return topic_name


def to_stream_tar(msg, producer, topic_name):
    try:
        time.sleep(5)
        producer.produce(topic_name, value=bytes(msg, "utf-8"))
        producer.flush()
    except Exception as e:
        logging.error(f"Problem {e} with {msg}")


# Consuming side
CONSUMER_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'testo',
    'auto.offset.reset': 'earliest',
}

# Producing side
KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092"
}

if __name__ == "__main__":
    # Kafka things
    consumer = Consumer(CONSUMER_CONFIG)
    last_topic = list_topics(consumer)
    logging.info(f"Subscribed to {last_topic}")
    consumer.subscribe([last_topic])
    client = admin.AdminClient(KAFKA_CONFIG)
    producer = Producer(KAFKA_CONFIG)
    topic_name = to_stream_dir(client)
    
    while True:
        msg = consumer.poll(timeout=10)  # Previously=120
        if msg:
            data = get_message(msg)
            logging.info(f"Consuming {data['objectId']} - {data['candidate']['jd']}")
            new_msg = "{}_{}".format(data['objectId'], data['candidate']['jd'])
            # Do something with data

            # Post data to new topic called MgC
            to_stream_tar(new_msg, producer, topic_name)

        else:
            last_topic = list_topics(consumer)
            consumer.subscribe([last_topic])
