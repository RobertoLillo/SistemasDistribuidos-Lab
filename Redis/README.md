# Redis installation commands (Redis latest)

## Docker

### Installation commands
```
$ sudo apt-get install docker.io

$ sudo docker pull redis

$ sudo docker run --name redis -d redis
```

### Service commands
```
$ sudo docker start/ps/stop
```

### Shell interface
```
$ sudo docker exec -it redis sh

# redis-cli

# ping
```
