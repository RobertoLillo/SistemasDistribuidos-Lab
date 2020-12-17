# Cassandra installation commands (Cassandra 4.0)

## Docker

### Installation commands
```
$ sudo apt-get install docker.io

$ sudo docker pull cassandra:4.0

$ sudo docker run -d --name cassandra -p 9042:9042 cassandra:4.0
```

### Service commands
```
$ sudo docker start/ps/stop
```

### Shell interface
```
$ sudo docker exec -it cassandra bash

# cqlsh
```

## Linux

### Installation commands
```
$ sudo apt-get install curl openjdk-11-jre-headless

$ echo "deb http://downloads.apache.org/cassandra/debian 40x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list

$ curl https://downloads.apache.org/cassandra/KEYS | sudo apt-key add -

$ sudo apt-get update

$ sudo apt-get install cassandra
```

### Service commands
```
$ sudo service cassandra start/status/stop
```

### Shell interface
```
$ cqlsh
```