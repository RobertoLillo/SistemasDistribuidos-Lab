/*
CREATE KEYSPACE

Inside a keyspace you can have many tables.
*/
CREATE KEYSPACE IF NOT EXISTS test_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};

/*
USE KEYSPACE
*/
USE test_keyspace;

/*
CREATE TABLE INSIDE KEYSPACE

A table contains a set of rows which contain many key-value pair columns.
Every row has a primary key (COMPOSITE KEY) specified for data access.
*/
CREATE TABLE IF NOT EXISTS text_table_by_id (uid uuid PRIMARY KEY, test_text text);

/*
CREATE TABLE INSIDE KEYSPACE WITH PARTITION KEY AND CLUSTERING COLUMN

COMPOSITE KEY: made up from a PARTITION KEY and a number of CLUSTERING COLUMNS.
PARTITION KEY: identify the node where the data is stored.
CLUSTERING COLUMN: used for sorting and to order data stored on disk.

text_maker is not unique as id so a COMPOSITE KEY is needed, where the combination of text_maker and id makes a unique key.

PRIMARY KEY(PARTITION KEY, CLUSTERING COLUMN)
*/
CREATE TABLE IF NOT EXISTS text_table_by_maker (text_maker text, uid uuid, PRIMARY KEY(text_maker, uid));

/*
INSERT INTO TABLES

You can leave blank spaces in the table.
*/
INSERT INTO text_table_by_id (uid, test_text) VALUES (uuid(), 'test_text_1');
INSERT INTO text_table_by_id (uid, test_text) VALUES (uuid(), 'test_text_2');
INSERT INTO text_table_by_id (uid, test_text) VALUES (uuid(), 'test_text_3');

INSERT INTO text_table_by_maker (text_maker, uuid()) VALUES ('maker_1', 1);
INSERT INTO text_table_by_maker (text_maker, uuid()) VALUES ('maker_2', 2);
INSERT INTO text_table_by_maker (text_maker, uuid()) VALUES ('maker_1', 3);

/*
SELECT FROM TABLES

Always query data using the PRIMARY KEY or PARTITION KEY.
Use CLUSTERING COLUMNS for ORDER BY.
*/
SELECT * FROM text_table_by_id;
SELECT * FROM text_table_by_id WHERE id=1;

SELECT * FROM text_table_by_maker;
SELECT * FROM text_table_by_maker WHERE text_maker='maker_1';
SELECT * FROM text_table_by_maker WHERE text_maker='maker_1' ORDER BY uid;

----------------------------------------------------------------------------

CREATE KEYSPACE IF NOT EXISTS astro_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};

CREATE TABLE IF NOT EXISTS nearly_black (id text PRIMARY KEY, jd float, date date);
CREATE TABLE IF NOT EXISTS statistics (id text PRIMARY KEY, jd float, date date)