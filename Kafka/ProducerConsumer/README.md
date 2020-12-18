# Sistemas Distribuidos

## INFO-USACH-13228-AY

### 

## Requerimientos
Para la ejecución de scripts es necesario tener instalado:

- Python 3.X
- Docker
- Docker-compose

**Nota:** Se recomienda utilizar algún entorno virtual ([conda](https://docs.anaconda.com/anaconda/install/) o [virtualenv](https://virtualenv.pypa.io/en/stable/)) para instalar librerías mediante `pip`. 

Luego se debe instalar las librerías a utilizar, 

```bash
git clone https://github.com/JavierArredondo/INFO-USACH-13228-AY.git
cd INFO-USACH-13228-AY/
pip install -r requirements.txt
```

## Ejecución de scripts
En primer lugar deben inicializar el ambiente de trabajo de Kafka y Zookeper.

```bash
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

Finalmente deben ejecutar los scripts correspondientes, por ejemplo para el grupo de reddit:

- Productor
```bash
python reddit/toad.py
```

- Consumidor
```bash
python reddit/frog.py
```

La idea es que ejecuten tanto el Productor y Consumidor al mismo tiempo y vean los outputs en cada terminal.

###########################################################################################################################

# Witsi witsi araña
Para ejecutar el Productor en forma de desarrollo es necesario tener descargado algunos archivos `tar.gz` en un directorio data. La recomendación es ir a la página de [ZTF Archive](https://ztf.uw.edu/alerts/public/) y descargar archivos razonablemente livianos.
Los pasos a seguir serían:

```bash
mkdir data
cd data
wget https://ztf.uw.edu/alerts/public/ztf_public_20200330.tar.gz
```

Luego ejecutar el script
```bash
python breeder.py
``` 

Si ejecutan el script de un servidor, es posible que el script realice la tarea de descargar los n-últimos archivos. Para descargar los últimos 5 archivos deben ejecutar:
```bash
python breeder.py 5
```
