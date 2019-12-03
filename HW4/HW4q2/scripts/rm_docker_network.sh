#!/bin/bash

container1=$1
container2=$2
network=$1"_"$2

docker network disconnect $network $container1
docker network disconnect $network $container2
docker network rm $network
