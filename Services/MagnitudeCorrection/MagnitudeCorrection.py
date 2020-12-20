from confluent_kafka import admin, Producer, Consumer
import logging
import time 
import io

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s.%(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def list_topics(c: Consumer, filter_by="ZTF-"):
    topics = c.list_topics().topics.keys()
    return list(filter(lambda x: filter_by in x, list(topics)))[-1]


def to_stream_dir(kafka_client):
    topic_name = "MgC-Topic1"
    new_topic = admin.NewTopic(topic_name, 1, 1)
    kafka_client.create_topics([new_topic])
    logging.info(f"Creating topic {topic_name}")
    return topic_name


def to_stream_tar(msg, producer, topic_name):
    try:
        logging.info(f"Producing {msg}")
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
            # Do something with data
            logging.info(f"Consuming {msg.value().decode(encoding='UTF-8')}")

            # Post data to new topic called MgC
            real_msg = msg.value().decode(encoding='UTF-8') + "Correction"
            to_stream_tar(real_msg, producer, topic_name)

        else:
            last_topic = list_topics(consumer)
            consumer.subscribe([last_topic])
