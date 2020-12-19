# KAFKA

## Ejecución de scripts
En primer lugar deben inicializar el ambiente de trabajo de Kafka y Zookeper.

```
docker-compose up -d
```

Para verificar que los servicios están ejecutándose:

```bash
docker-compose ps
```

``` bash
             Name                            Command               State                   Ports                 
-----------------------------------------------------------------------------------------------------------------
info-usach-13228-ay_kafka_1       /opt/bitnami/scripts/kafka ...   Up      0.0.0.0:9092->9092/tcp                
info-usach-13228-ay_zookeeper_1   /opt/bitnami/scripts/zooke ...   Up      2181/tcp, 2888/tcp, 3888/tcp, 8080/tcp
```