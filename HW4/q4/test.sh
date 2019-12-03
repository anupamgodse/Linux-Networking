#!/bin/bash

plugin=$1

for i in {1..10}
do
 echo "server" > logs/${plugin}_${i}_server.log
 echo "client" > logs/${plugin}_${i}_client.log
done
