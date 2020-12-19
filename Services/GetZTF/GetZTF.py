from confluent_kafka import admin, Producer
import logging
import time


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s.%(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092"
}


def to_stream_dir(kafka_client):
    producer = Producer(KAFKA_CONFIG)
    topic_name = "ZTF-Topic1"
    new_topic = admin.NewTopic(topic_name, 1, 1)
    kafka_client.create_topics([new_topic])
    logging.info(f"Creating topic {topic_name}")
    to_stream_tar(producer, topic_name)


def to_stream_tar(producer, topic_name):
    auxList = ["TEXT0", "TEXT1", "TEXT2", "TEXT3", "TEXT4"]
    try:
        for msg in auxList:
            logging.info(f"Producing {msg}")
            time.sleep(5)
            producer.produce(topic_name, value=bytes(msg, "utf-8"))
            producer.flush()
    except Exception as e:
        logging.error(f"Problem {e} with {msg}")


if __name__ == "__main__":
    # Kafka things
    client = admin.AdminClient(KAFKA_CONFIG)
    to_stream_dir(client)
