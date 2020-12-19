# Light Curve Calculation

- Instalar las librerías necesarias.
```
pip3 install -r requirements.txt
```

- Ejecutar el consumidor.
```
python3 LightCurve.py
```

Este consumirá información desde el tópico Kafka con el nombre _____ y guardará la información en la base de datos Cassandra en localhost en la tabla light_curve_by_id.