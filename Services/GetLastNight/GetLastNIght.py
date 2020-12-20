import redis
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy

REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
REDIS_PASSWORD = ''

if __name__ == "__main__":
    # Cassandra things
    clusterCassandra = Cluster(contact_points=['127.0.0.1'], port=9042, protocol_version=4,
                    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='datacenter1'))
    sessionCassandra = clusterCassandra.connect('test_keyspace')

    # Redis things
    redisConnection = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    # Getting the Data from Cassandra
    # Get and store the last inserted item in Cassandra.
    lastNight = sessionCassandra.execute("SELECT * FROM text_table_by_id").all()[-1]

    print(str(lastNight.uid), lastNight.test_text)

    try:
      lastNightArray = [str(lastNight.uid), lastNight.test_text]
      redisConnection.lpush('lastNight', *lastNightArray)
    except Exception as e:
      print(e)