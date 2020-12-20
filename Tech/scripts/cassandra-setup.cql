CREATE KEYSPACE IF NOT EXISTS test_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};

USE test_keyspace;

CREATE TABLE IF NOT EXISTS text_table_by_id (uid uuid PRIMARY KEY, test_text text);
CREATE TABLE IF NOT EXISTS light_curve_by_id (uid uuid PRIMARY KEY, test_text text);
