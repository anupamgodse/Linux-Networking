#!/bin/bash

container=$1

docker container stop $container
docker container rm $container
