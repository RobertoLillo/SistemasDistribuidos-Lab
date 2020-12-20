#!/usr/bin/env bash

cqlsh -f /scripts/cassandra-setup.cql cassandra
echo "### SETUP LISTO! ###"