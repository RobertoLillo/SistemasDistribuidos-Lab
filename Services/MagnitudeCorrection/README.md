# Magnitude Correction

- Instalar las librerías necesarias.
```
pip3 install -r requirements.txt
```

- Ejecutar el consumidor.
```
python3 MagnitudeCorrection.py
```

Este consumirá información desde el tópico Kafka con el nombre "ztf - ..." e ingresará la información en el tópico "MgC - ...".