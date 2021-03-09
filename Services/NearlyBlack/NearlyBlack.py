from confluent_kafka import Consumer
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
import logging
import fastavro
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


if __name__ == "__main__":
    # Cassandra things
    cluster = Cluster(contact_points=['127.0.0.1'], port=9042, protocol_version=4,
                    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='datacenter1'))
    session = cluster.connect('astro_keyspace')

    # Kafka things
    consumer = Consumer(CONSUMER_CONFIG)
    last_topic = list_topics(consumer)
    logging.info(f"Subscribed to {last_topic}")
    consumer.subscribe([last_topic])

    while True:
        msg = consumer.poll(timeout=10)  # Previously=120
        if msg:
            data = get_message(msg)
            logging.info(f"Consuming {data['objectId']} - {data['candidate']['jd']}")
            # Do something with data

            # Sending data to Cassandra database
            session.execute("INSERT INTO nearly_black (id, jd, date) VALUES (%s, %s, todate(now()))", [data['objectId'], data['candidate']['jd']])

        else:
            last_topic = list_topics(consumer)
            consumer.subscribe([last_topic])
