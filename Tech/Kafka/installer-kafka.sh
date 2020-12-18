#!/bin/bash

set -eu -o pipefail # fail on error , debug all lines

sudo -n true
test $? -eq 0 || exit 1 "Se necesitan privilegios para correr el script"


echo --------------------------------
echo Configurando usuario de kafka
adduser --system --no-create-home --disabled-password --disabled-login kafka
echo --------------------------------
echo Descargando binarios de kafka ....
mkdir kafka 
cd kafka
wget 'https://downloads.apache.org/kafka/2.6.0/kafka_2.13-2.6.0.tgz'
tar -xvzf kafka_2.13-2.6.0.tgz  --strip-components 1
rm -rf kafka_2.13-2.6.0.tgz

echo --------------------------------
echo Instalación terminada
sleep 6
