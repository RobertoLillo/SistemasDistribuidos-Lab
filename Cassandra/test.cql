/*
CREATE KEYSPACE

Inside a keyspace you can have many tables.
*/
CREATE KEYSPACE IF NOT EXISTS test_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};

/*
DROP KEYSPACE
*/
DROP KEYSPACE test_keyspace;

/*
USE KEYSPACE
*/
USE test_keyspace;

/*
CREATE TABLE INSIDE KEYSPACEs

A table contains a set of rows which contain many key-value pair columns.
Every row has a primary key (COMPOSITE KEY) specified for data access.
*/
CREATE TABLE IF NOT EXISTS text_table_by_id (id int PRIMARY KEY, test_text text);

/*
CREATE TABLE INSIDE KEYSPACE WITH PARTITION KEY AND CLUSTERING COLUMN

COMPOSITE KEY: made up from a PARTITION KEY and a number of CLUSTERING COLUMNS.
PARTITION KEY: identify the node where the data is stored.
CLUSTERING COLUMN: used for sorting and to order data stored on disk.

text_maker is not unique as id so a COMPOSITE KEY is needed, where the combination of text_maker and id makes a unique key.

PRIMARY KEY(PARTITION KEY, CLUSTERING COLUMN)
*/
CREATE TABLE IF NOT EXISTS txst_table_by_maker (text_maker text, id int, PRIMARY KEY(text_maker, id));

/*
DROP TABLE
*/
DROP TABLE text_table_by_id;